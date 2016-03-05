# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from modeltranslation.admin import TranslationGenericStackedInline, TranslationAdmin
from core.utils import TranslationTabsMixin
import core.metatags.translation
from .models import MetaTag
from .forms import InlineMetaTagForm, MetaTagForm


class MetaTagInline(TranslationGenericStackedInline):
    model = MetaTag
    extra = 1
    max_num = 1
    form = InlineMetaTagForm


class MetaTagAdmin(TranslationAdmin, TranslationTabsMixin):
    form = MetaTagForm
    list_display = ('url',)

    def queryset(self, request):
        qs = super(MetaTagAdmin, self).get_queryset(request)
        return qs.filter(content_type__isnull=True, object_id__isnull=True)


admin.site.register(MetaTag, MetaTagAdmin)
