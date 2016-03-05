# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions

from .models import Slide

class SlideTranslationOptions(TranslationOptions):
    fields = ('top_text', 'bottom_text')

translator.register(Slide, SlideTranslationOptions)
