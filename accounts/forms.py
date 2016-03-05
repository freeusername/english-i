from django.shortcuts import redirect
from django import forms
from django.template import loader
from django.contrib import auth
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.forms.widgets import TextInput
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .models import User

class RegistrationForm(forms.ModelForm):
    """
    Users registration form
    """
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'inputs',
        }),
        required=True,
        error_messages={
            "required": _('Enter First name.'),
        },
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'inputs',
        }),
        required=True,
        error_messages={
            "required": _('Enter Last name.'),
        },
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'inputs',
        }),
        required=True,
        error_messages={
            "required": _('Enter Email.'),
        },
    )

    class Meta:
        model = User
        label = ('first_name', 'last_name', 'email')
        exclude = ('username', 'is_staff', 'is_active', 'date_joined', 'password', 'last_login', 'is_active')

    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_('This email address is already in use.'))

        return self.cleaned_data['email']


class AuthenticationForm(auth_forms.AuthenticationForm):
    username = forms.CharField(
        max_length=255,
        widget=TextInput(
            attrs={
                'class': 'inputs',
            }
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'inputs',
            }
        ),
    )
    remember_me = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'checkboxes'
            }
        ),
        required=False,
    )

    user_cache = None

    def save(self, request):
        cd = self.cleaned_data
        user = self.user_cache
        auth.login(request, user)
        if not 'remember_me' in cd or not cd['remember_me']:
            request.session.set_expiry(0)
        return user


class UserEditForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'password_incorrect': _("Your old password was entered incorrectly. "
                                "Please enter it again."),
    }
    old_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'inputs'}))
    new_password1 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'inputs'}),
        label=_('New password'),
    )
    new_password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'inputs'}),
    )
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'inputs'}),
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'inputs'}),
    )

    class Meta:
        model = User
        exclude = (
            'is_superuser',
            'is_active',
            'date_joined',
            'last_login',
            'password',
            'username'
        )
        fields = (
            'avatar', 'first_name', 'last_name', 'phone', 'skype', 'city', 'company', 'email', 'old_password', 'new_password1', 'new_password2'
        )
        widgets = {
            'avatar': forms.FileInput(),
            # 'first_name': forms.TextInput(attrs={'class': 'inputs'}),
            # 'last_name': forms.TextInput(attrs={'class': 'inputs'}),
            'phone': forms.TextInput(attrs={'class': 'inputs'}),
            'skype': forms.TextInput(attrs={'class': 'inputs'}),
            'city': forms.TextInput(attrs={'class': 'inputs'}),
            'company': forms.TextInput(attrs={'class': 'inputs'}),
            'email': forms.TextInput(attrs={'class': 'inputs'}),
        }

    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data['old_password']
        if old_password and not self.instance.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password

    def clean_new_password2(self):
        old_password = self.cleaned_data.get('old_password')
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if old_password and password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2


class PayInvoice(forms.Form):
    id_invoice = forms.CharField(
        widget=forms.TextInput(),
    )


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.TextInput(attrs={'class': 'inputs', 'placeholder': _('Email')}))

    def save(self, domain_override=None,
             subject_template_name='accounts/mail/password_reset_subject.txt',
             email_template_name='accounts/mail/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None):
        """
        Generates a one-use only link for resetting password and sends to the
        user.
        """
        from django.core.mail import send_mail
        UserModel = get_user_model()
        email = self.cleaned_data["email"]
        active_users = UserModel._default_manager.filter(
            email__iexact=email, is_active=True)
        for user in active_users:
            # Make sure that no email is sent to a user that actually has
            # a password marked as unusable
            if not user.has_usable_password():
                continue
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            c = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': 'https' if use_https else 'http',
            }
            subject = loader.render_to_string(subject_template_name, c)
            # Email subject *must not* contain newlines
            subject = ''.join(subject.splitlines())
            email = loader.render_to_string(email_template_name, c)

            if html_email_template_name:
                html_email = loader.render_to_string(html_email_template_name, c)
            else:
                html_email = None
            send_mail(subject, email, from_email, [user.email], html_message=html_email)


class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    new_password1 = forms.CharField(label=_("New password"),
                                    widget=forms.PasswordInput(attrs={'class': 'inputs'}))
    new_password2 = forms.CharField(label=_("New password confirmation"),
                                    widget=forms.PasswordInput(attrs={'class': 'inputs'}))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user