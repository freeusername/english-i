# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

from core.metatags.admin import MetaTagInline
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from core.utils.forms import AdminFileThumbWidget

import pages.translation
from .models import Page


@admin.register(Page)
class PageAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'url')
    inlines = [MetaTagInline]
