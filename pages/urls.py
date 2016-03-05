# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('pages.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^courses/$', 'courses_list', name='courses_list'),
                       url(r'^team/$', 'team', name='team'),
                       url(r'^explore/$', 'explore', name='explore'),
                       )
