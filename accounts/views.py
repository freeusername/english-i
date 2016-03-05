from decimal import Decimal
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import auth
from django.contrib.sites.models import Site
from django.contrib.auth.tokens import default_token_generator
from django.views.generic.base import TemplateView
from django.views.decorators.cache import never_cache
from django.template.response import TemplateResponse
from django.forms.formsets import formset_factory
from django.shortcuts import render, redirect, resolve_url
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponseRedirect

from registration import signals
from registration.models import RegistrationProfile
from registration.views import ActivationView as BaseActivationView
from djlime.utils.mail import send_mail

from payments.utils import order2json, get_password
from payments.crypto import encrypt
from payments.models import PaymentOrder, BACKEND_LIQPAY

from .models import UserCourse, User
from .forms import AuthenticationForm, RegistrationForm, UserEditForm, PayInvoice, SetPasswordForm
from invoices.models import Invoice, decode_sum
from liqpay.integration import LiqPayIntegration
from liqpay import models as lp_models
from pages.views import get_page

ORDER_ID = 'ORDER_PK'


def registration(request):
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            password = User.objects.make_random_password()
            site = Site.objects.get_current()
            cleaned_data['username'] = cleaned_data['email']
            # cleaned_data['password'] = password
            new_user = RegistrationProfile.objects.create_inactive_user(
                form=form,
                site=site,
                send_email=False,
            )
            new_user.set_password(password)
            new_user.first_name = cleaned_data['first_name']
            new_user.last_name = cleaned_data['last_name']
            new_user.phone = ''
            new_user.city = ''
            new_user.company = ''
            new_user.skype = ''
            new_user.save(update_fields=['first_name',
                                         'last_name',
                                         'phone',
                                         'city',
                                         'company',
                                         'skype',
                                         'password'])
            registration_profile = RegistrationProfile.objects.get(user=new_user)
            ctx_dict = {
                'site': site,
                'user': new_user,
                'password': password,
                'activation_key': registration_profile.activation_key,
            }
            user_email = u"{0} <{1}>".format(new_user.full_name, new_user.email)

            send_mail(user_email,
                      'accounts/mail/activation_email_subject.txt',
                      'accounts/mail/activation_email.html',
                      'accounts/mail/activation_email.txt',
                      ctx_dict)
            signals.user_registered.send(sender=None, user=new_user, request=request)
            if request.is_ajax():
                to = reverse('registration_complete')
                return JsonResponse({'success': True, 'location': to})
            return redirect('registration_complete')
        else:
            if request.is_ajax():
                errors = dict([(k, force_text(v[0])) for k, v in form.errors.items()])
                return JsonResponse({'success': False, 'errors': errors})
    else:
        form = RegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})


@never_cache
def login(request, template_name='accounts/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm):
    """
    Displays the login form and handles the login action.
    """
    if request.user.is_authenticated():
        return redirect('home')
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():
            # # Ensure the user-originating redirection url is safe.
            # if not is_safe_url(url=redirect_to, host=request.get_host()):
            #     redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())
            if not redirect_to:
                redirect_to = reverse('home')
            if request.is_ajax():
                return JsonResponse({'success': True, 'location': redirect_to})
            return HttpResponseRedirect(redirect_to)
        else:
            if request.is_ajax():
                errors = dict([(k, force_text(v[0])) for k, v in form.errors.items()])
                return JsonResponse({'success': False, 'errors': errors})
    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    return TemplateResponse(request, template_name, context)


def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def profile(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user, })


@login_required
def my_courses(request):
    courses = UserCourse.objects.filter(user=request.user)
    return render(request, 'accounts/profile_courses.html', {'courses': courses})


@login_required
def profile_payments(request):
    p_invoices = Invoice.objects.filter(status='invoice_paid', user=request.user)
    np_invoices = Invoice.objects.filter(status='invoice_notpaid', user=request.user)
    len_invoices = len(np_invoices)
    form_set = formset_factory(PayInvoice, extra=len_invoices, max_num=len_invoices)
    if request.method == "POST":
        form_set = form_set(request.POST)
        if form_set.is_valid():
            n = 0
            while n < len_invoices:
                cd = form_set.cleaned_data[n]
                n += 1
                if len(cd) >= 1:
                    # pk_invoice = cd['id_invoice']
                    invoice = Invoice.objects.get(pk=cd['id_invoice'])
                    lang = get_language()
                    if lang == 'en':
                        pro_sum = invoice.price
                        currency = lp_models.LIQPAY_CCY_USD
                        if invoice.user != request.user:
                            return JsonResponse({'success': False, 'errors': "Not found invoice"})
                    else:
                        # getcontext().prec = 2
                        pro_sum = invoice.get_price_ru
                        currency = lp_models.LIQPAY_CCY_UAH
                        # sum = format(invoice.get_price_ru)
                        # sum.quantize(-2)
                        if invoice.user != request.user:
                            return JsonResponse({'success': False, 'errors': "Not found invoice"})
                    order = PaymentOrder.objects.create(
                        user=request.user,
                        sum=pro_sum,
                        backend=BACKEND_LIQPAY,
                        invoice=invoice,
                    )
                    order_json = order2json(order)
                    order_crypted = encrypt(get_password(), order_json)
                    amount = pro_sum
                    description = _('Paying to %s') % invoice
                    request.session[ORDER_ID] = order.pk
                    liqpay_form = LiqPayIntegration({"currency": currency,
                                                     "amount": amount,
                                                     "description": description,
                                                     "language": lang,
                                                     "order_id": order_crypted}).cnb_form()
                    return JsonResponse({'success': True,
                                         'liqpay_form': liqpay_form})
        else:
            return JsonResponse({'success': False, 'errors': "Not found or incorrect invoice amount"})
    return render(request, 'accounts/profile_payments.html', {'p_invoices': p_invoices,
                                                              'np_invoices': np_invoices,
                                                              'form_set': form_set})


@login_required
def thank_you(request):
    page = get_page(request, '/profile/payments/complete/')
    order_id = request.session.get(ORDER_ID, 0)
    template = 'pages/payment_complete.html'
    try:
        order = PaymentOrder.objects.get(pk=order_id)
    except PaymentOrder.DoesNotExist:
        return redirect('home')
    request.session[ORDER_ID] = 0
    return render(request, template, {'order': order,
                                      'page': page})


@login_required
def profile_edit(request):
    user = request.user
    form = UserEditForm(request.POST or None, request.FILES or None, instance=user)
    if request.method == "POST":
        if form.is_valid():
            account = form.save(commit=False)
            if form.cleaned_data['new_password1'] and form.cleaned_data['new_password2']:
                password = form.cleaned_data['new_password2']
                account.set_password(password)
            account.save()
            # to = reverse('profile_edit')

            if request.is_ajax():
                return JsonResponse({'success': True})
        else:
            if request.is_ajax():
                errors = dict([(k, force_text(v[0])) for k, v in form.errors.items()])
                return JsonResponse({'success': False, 'errors': errors})
    return render(request, 'accounts/profile_edit.html', {'form': form})


@never_cache
def password_reset_confirm(request, uidb64=None, token=None,
                           template_name='accounts/password_reset_confirm.html',
                           token_generator=default_token_generator,
                           set_password_form=SetPasswordForm,
                           post_reset_redirect='accounts_password_complete',
                           current_app=None, extra_context=None):
    """
    View that checks the hash in a password reset link and presents a
    form for entering a new password.
    """
    UserModel = get_user_model()
    assert uidb64 is not None and token is not None  # checked by URLconf
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_complete')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    try:
        # urlsafe_base64_decode() decodes to bytestring on Python 3
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True
        title = _('Enter new password')
        if request.method == 'POST':
            form = set_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                to = reverse('accounts_password_complete')
                if request.is_ajax():
                    return JsonResponse({'success': False, 'location': to})
                return HttpResponseRedirect(to)
            else:
                if request.is_ajax():
                    errors = dict([(k, force_text(v[0])) for k, v in form.errors.items()])
                    return JsonResponse({'success': False, 'errors': errors})
        else:
            form = set_password_form(user)
    else:
        validlink = False
        form = None
        title = _('Password reset unsuccessful')
    context = {
        'form': form,
        'title': title,
        'validlink': validlink,
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)
