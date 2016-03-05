# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('courses.views',
    url(r'^courses/(?P<slug>[-\w]+)/$', 'course_view', name='course_view'),
    url(r'^skill/(?P<pk>\d+)/$', 'skill_view', name='skill_view'),
    url(r'^course/create/$', 'create_personal_course', name='create_personal_course'),
    url(r'^course/create/help/$', 'course_create_help', name='course_create_help'),
    url(r'^course/price/(?P<pk>\d+)/$', 'course_prices', name='course_prices'),
    url(r'^course/subscribe/(?P<pk>\d+)/$', 'front_course_subscribed', name='front_course_subscribed'),
)
