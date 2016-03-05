# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions

from .models import Invoice


class InvoiceTranslationOptions(TranslationOptions):
    fields = ()

translator.register(Invoice, InvoiceTranslationOptions)
