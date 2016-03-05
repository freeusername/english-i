from django.shortcuts import render, redirect
from django.contrib.sites.models import get_current_site
from django.contrib.auth.decorators import login_required
import re
from django.forms.formsets import formset_factory
from django.utils.translation import pgettext

from django.contrib.auth.models import Group
from core.configs.models import AppConfig
from core.utils.helpers import group_of, clean_sting, send_mail, get_grammatical_case
from .models import Course, Intensity, Skill, Duration
from .forms import CreatePersonCourseForm, ChangePriceForm
from accounts.models import UserCourse, User
from invoices.models import Invoice, decode_sum
from pages.views import get_page


# @login_required
def course_view(request, slug):
    course = Course.objects.get(slug=slug)
    subscribe = False
    if request.user.is_authenticated():
        subscribe = UserCourse.objects.filter(user=request.user, course=course)
    return render(request, 'courses/course_view.html', {'course': course,
                                                        'subscribe': subscribe})


@login_required
def skill_view(request, pk):
    skill = Course.objects.get(pk=pk)
    return render(request, 'courses/skill_view.html', {'skill': skill})


@login_required
def create_personal_course(request):
    page = get_page(request, '/course/create/')
    skills = Skill.objects.all()
    skills = group_of(skills, 2)
    if request.method == "POST":
        form = CreatePersonCourseForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data['no_skills']:
                form.save()
                course = Course.objects.get(id=form.instance.id)
                course.user = request.user
                course.value_type = 'course_personal'
                course.save()
                subscribe = UserCourse.objects.create(
                    user=request.user,
                    course=course,
                    status='course_notpaid'
                )
                subscribe.save()
                invoice = Invoice.objects.create(
                    user=request.user,
                    course=subscribe,
                    status='invoice_noprice'
                )
                invoice.save()
                return redirect('/course/price/%s/' % invoice.pk)
            else:
                form.save()
                course = Course.objects.get(id=form.instance.id)
                course.user = request.user
                course.value_type = 'course_personal'
                course.save()
                subscribe = UserCourse.objects.create(
                    user=request.user,
                    course=course,
                    status='course_notpaid'
                )
                subscribe.save()
                invoice = Invoice.objects.create(
                    user=request.user,
                    course=subscribe,
                    status='invoice_noprice'
                )
                invoice.save()
                managers = User.objects.filter(
                    groups=Group.objects.get(
                        id=AppConfig.objects.get(
                            key='id_group_managers', enabled=True).value), is_staff=True).values_list('email')
                addresses = re.sub("^|\[|\]|\(u|\'\,|\)|\'|\s+|\n|\r|\s+$", '', str(managers))
                recipients = [x.strip() for x in clean_sting(addresses).split(',')]
                site = get_current_site(request)
                ctx_dict = {
                    'site': site,
                    'user': request.user,
                    'course': course,
                }
                send_mail(recipients,
                          'courses/mail/signal_email_subject.txt',
                          'courses/mail/signal_email.html',
                          'courses/mail/signal_email.txt',
                          ctx_dict)
                return redirect('/course/price/%s/' % invoice.pk)
    else:
        form = CreatePersonCourseForm()
    return render(request, 'courses/create_course.html', {'form': form,
                                                          'skills': skills,
                                                          'page': page})


@login_required
def course_prices(request, pk):
    invoice = Invoice.objects.get(pk=pk)
    if invoice.user == request.user and invoice.status == u'invoice_notpaid' and invoice.price:
        return redirect('/profile/payments/')
    skills = invoice.course.course.skills.all()
    lessons = 0
    for item in skills:
        lessons += item.lessons
    lessons = get_grammatical_case(lessons, pgettext('1', 'lesson'), pgettext('2-4', 'lessons'), pgettext('5+', 'lessons'))
    intensities = Intensity.objects.all()
    len_intensities = len(intensities)
    form_set = formset_factory(ChangePriceForm, extra=len_intensities, max_num=len_intensities)
    if request.method == "POST":
        form_set = form_set(request.POST)
        if form_set.is_valid():
            n = 0
            while n < len_intensities:
                cd = form_set.cleaned_data[n]
                n += 1
                if len(cd) >= 1:
                    subscribe = invoice.course
                    subscribe.duration = Duration.objects.get(pk=cd['duration_id'])
                    subscribe.intensity = Intensity.objects.get(pk=cd['intensity_id'])
                    subscribe.save(update_fields=['duration', 'intensity'])
                    invoice.price = decode_sum(cd['price'])
                    invoice.status = 'invoice_notpaid'
                    invoice.save(update_fields=['price', 'status'])
            if invoice.course.course.no_skills:
                return redirect('/course/create/help/')
            else:
                return redirect('/profile/payments/')
    else:
        form_set = form_set()
    return render(request, 'courses/course_price.html', {'intensities': intensities,
                                                         'form_set': form_set,
                                                         'invoice': invoice,
                                                         'skills': skills,
                                                         'lessons': lessons})


def course_create_help(request):
    page = get_page(request, '/course/create/help/')
    return render(request, 'pages/course_create_help.html', {'page': page})


@login_required
def front_course_subscribed(request, pk):
    course = Course.objects.get(pk=pk)
    if UserCourse.objects.filter(user=request.user, course=course):
        return redirect('/profile/courses/')
    else:
        subscribe = UserCourse.objects.create(
            user=request.user,
            course=course,
            status='course_notpaid'
        )
        subscribe.save()
        invoice = Invoice.objects.create(
            user=request.user,
            course=subscribe,
            status='invoice_notpaid',
            price=course.price,
        )
        invoice.save()
        return redirect('/profile/payments/')