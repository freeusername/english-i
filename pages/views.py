# -*- coding: utf-8 -*-
import simplejson
import json
from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect
from djlime.utils.pagination import paginator_factory
from django.contrib.sites.models import get_current_site
from django.core.urlresolvers import reverse
from django.utils.encoding import force_text
from django.contrib.auth.decorators import login_required

from .models import Page
from core.configs.models import AppConfig
from core.utils.helpers import clean_sting, send_mail
from core.utils.views import JsonResponse
from slides.models import Slide
from courses.models import Course
from testimonials.models import Testimonial, Teacher


def get_page(request, url, raw=False):
    if not url.startswith('/'):
        url = "/" + url

    language = request.LANGUAGE_CODE
    language_prefix = '/%s' % language

    if url.startswith(language_prefix):
        url = url[len(language_prefix):]

    try:
        if raw:
            kwargs = {
                '{0}__{1}'.format('url', 'exact'): url
            }
        else:
            kwargs = {
                'enabled': True,
                '{0}__{1}'.format('url', 'exact'): url
            }
        page = get_object_or_404(Page, **kwargs)
    except Http404:
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
            try:
                if raw:
                    kwargs = {
                        '{0}__{1}'.format('url', 'exact'): url
                    }
                else:
                    kwargs = {
                        'enabled': True,
                        '{0}__{1}'.format('url', 'exact'): url
                    }
                page = get_object_or_404(Page, **kwargs)
            except Http404:
                raise
        else:
            raise
    return page


def page(request, url):
    page = get_page(request, url)
    return render_page(request, page)


@csrf_protect
def render_page(request, page):
    if page.template:
        template = 'pages/{}.html'.format(page.template)
    else:
        template = 'pages/default.html'
    response = TemplateResponse(request, template, {'page': page})
    response.render()
    return response


def home(request):
    page = get_page(request, '/')
    slides = Slide.objects.filter(show=True)
    testimonials = Testimonial.objects.filter(show=True)
    return render(request, 'pages/home.html', {'page': page,
                                               'slides': slides,
                                               'testimonials': testimonials})


def courses_list(request):
    page = get_page(request, '/courses/')
    courses = Course.objects.filter(value_type='course_front')
    courses_featured = courses.filter(featured=True)
    courses_other = courses.filter(featured=False)
    return render(request, 'courses/courses_list.html', {'page': page,
                                                         'courses': courses,
                                                         'courses_featured': courses_featured,
                                                         'courses_other': courses_other})


def team(request):
    page = get_page(request, '/team/')
    teachers = Teacher.objects.filter(show=True)
    return render(request, 'pages/team.html', {'page': page,
                                               'teachers': teachers})


def explore(request):
    page = get_page(request, '/explore/')
    return render(request, 'pages/overview.html', {'page': page})