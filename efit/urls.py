# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from djlime.views.robots import RobotsView
from django.contrib.staticfiles.urls import static
from solid_i18n.urls import solid_i18n_patterns
from filebrowser.sites import site
from django.views.generic.base import RedirectView

from liqpay.integration import LiqPayIntegration

admin.autodiscover()

# js_info_dict = {
#     'domain': 'djangojs',
#     'packages': ('efit',),
# }

urlpatterns = patterns('',
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
    url(r'^robots\.txt$', RobotsView.as_view()),
    # url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/filebrowser/',include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^liqpay/', include(LiqPayIntegration().urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += solid_i18n_patterns('',
    url(r'^', include('pages.urls')),
    url(r'^', include('courses.urls')),
    url(r'^', include('accounts.urls')),
)
