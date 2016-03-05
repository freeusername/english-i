# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions

from .models import Testimonial, Teacher


class TestimonialTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'full_name', 'info')

class TeacherTranslationOptions(TranslationOptions):
    fields = ('description', 'full_name')


translator.register(Testimonial, TestimonialTranslationOptions)
translator.register(Teacher, TeacherTranslationOptions)
