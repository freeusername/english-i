# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions

from .models import Item


class ItemTranslationOptions(TranslationOptions):
    fields = ('title',)

# class SubitemTranslationOptions(TranslationOptions):
#     fields = ('title',)


translator.register(Item, ItemTranslationOptions)
# translator.register(Subitem, SubitemTranslationOptions)
