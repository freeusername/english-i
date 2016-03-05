from modeltranslation.translator import translator, TranslationOptions

from .models import AppConfig

class AppConfigTranslationOptions(TranslationOptions):
    fields = ('value_name', 'value_string_ml', 'value_text_ml', 'value_html_ml')

translator.register(AppConfig, AppConfigTranslationOptions)
