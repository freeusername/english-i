# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

import menu.translation
from .models import Item


# class SubitemInline(TranslationStackedInline):
#     model = Subitem
#     extra = 0


@admin.register(Item)
class ItemAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'link', 'position',)
    list_editable = ['position']
    # list_filter = ('location',)
    # inlines = [SubitemInline]


# @admin.register(HomeItem)
# class ItemAdmin(TabbedTranslationAdmin):
#     list_display = ('admin_thumbnail', 'title', 'link', 'position', 'show')
#     list_editable = ['position', 'show']
#     list_display_links = ('admin_thumbnail', 'title')
