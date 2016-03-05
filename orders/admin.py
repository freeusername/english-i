# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

from core.metatags.admin import MetaTagInline
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from core.utils.forms import AdminFileThumbWidget

import pages.translation
from .models import Order

#
# @admin.register(Order)
# class PageAdmin(admin.ModelAdmin):
#     list_display = ('__unicode__', 'created_at', 'user')