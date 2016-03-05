# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_complete

from .forms import PasswordResetForm, SetPasswordForm
# from .views import ActivationView, password_reset_confirm
from .views import password_reset_confirm
from registration.backends.model_activation.views import ActivationView
from efit.settings.prod import DEFAULT_FROM_EMAIL


urlpatterns = patterns('accounts.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^registration/$', 'registration', name='registration'),
    url(r'^registration/complete/$',
        TemplateView.as_view(
            template_name='accounts/registration_complete.html'
        ),
        name='registration_complete'),
    url(r'^activate/complete/$',
        TemplateView.as_view(
            template_name='accounts/activation_complete.html'
        ),
        name='registration_activation_complete'),
    url(r'^activate/(?P<activation_key>\w+)/$',
        ActivationView.as_view(),
        name='registration_activate'),

    url(r'^profile/$', 'profile', name='profile'),
    url(r'^profile/courses/$', 'my_courses', name='my_courses'),
    url(r'^profile/payments/complete/$', 'thank_you', name='thank_you'),
    url(r'^profile/payments/$', 'profile_payments', name='profile_payments'),
    url(r'^profile/edit/$', 'profile_edit', name='profile_edit'),
    url(r'^password/reset/$', password_reset, {'template_name': 'accounts/password_reset.html',
                                               'email_template_name': 'accounts/mail/password_reset_email.html',
                                               'subject_template_name': 'accounts/mail/password_reset_subject.txt',
                                               'password_reset_form': PasswordResetForm,
                                               'from_email': DEFAULT_FROM_EMAIL,
                                               'post_reset_redirect': 'accounts_password_done'},name='accounts_password_reset'),
    url(r'^password/reset/done/$', password_reset_done, {'template_name': 'accounts/password_reset_done.html'}, name='accounts_password_done'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'template_name': 'accounts/password_reset_confirm.html', 'set_password_form': SetPasswordForm, 'post_reset_redirect': 'accounts_password_complete'}, name='accounts_password_confirm'),
    url(r'^password/reset/complete/$', password_reset_complete, {'template_name': 'accounts/password_reset_complete.html'}, name='accounts_password_complete'),
)
