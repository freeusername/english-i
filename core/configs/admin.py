# -*- coding: utf-8 -*-
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationAdmin
from core.utils import TranslationTabsMixin
import core.configs.translation
from .models import AppConfig



class AppConfigAdmin(TranslationAdmin, TranslationTabsMixin):
    list_display = ('key', 'value_name', 'value_type', 'enabled', 'value')
    list_editable = ('enabled',)
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('enabled', 'value_type')
    fieldsets = (
        (None, {'fields': ('key', 'value_name', 'value_type', 'enabled')}),
        (None, {
            'classes': ('cls-boolean value_fields',),
            'fields': ('value_boolean',),
        }),
        (None, {
            'classes': ('cls-integer value_fields',),
            'fields': ('value_integer',),
        }),
        (None, {
            'classes': ('cls-float value_fields',),
            'fields': ('value_float',),
        }),
        (None, {
            'classes': ('cls-decimal value_fields',),
            'fields': ('value_decimal',),
        }),
        (None, {
            'classes': ('cls-link value_fields',),
            'fields': ('value_link',),
        }),
        (None, {
            'classes': ('cls-date value_fields',),
            'fields': ('value_date',),
        }),
        (None, {
            'classes': ('cls-datetime value_fields',),
            'fields': ('value_datetime',),
        }),
        (None, {
            'classes': ('cls-string value_fields',),
            'fields': ('value_string',),
        }),
        (None, {
            'classes': ('cls-string_ml value_fields',),
            'fields': ('value_string_ml',),
        }),
        (None, {
            'classes': ('cls-text value_fields',),
            'fields': ('value_text',),
        }),
        (None, {
            'classes': ('cls-text_ml value_fields',),
            'fields': ('value_text_ml',),
        }),
        (None, {
            'classes': ('cls-html value_fields',),
            'fields': ('value_html',),
        }),
        (None, {
            'classes': ('cls-html_ml value_fields',),
            'fields': ('value_html_ml',),
        }),
        (None, {
            'fields': ('created_at', 'updated_at')}
        ),
    )

    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
            '/static/configs/admin/js/configs_support.js',
        )
        # js.append('/static/modeltranslation/js/force_jquery.js')
        # js.append('http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js')
        # js.append('/static/modeltranslation/js/tabbed_translation_fields.js')
        # js.append('/static/configs/admin/js/configs_support.js')
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(AppConfig, AppConfigAdmin)
