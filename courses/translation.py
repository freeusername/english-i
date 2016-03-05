# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions

from .models import Course, Skill, Intensity, Duration


class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'short_description', 'pros_cons')

class SkillTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class IntensityTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

class DurationTranslationOptions(TranslationOptions):
    fields = ()


translator.register(Course, CourseTranslationOptions)
translator.register(Skill, SkillTranslationOptions)
translator.register(Intensity, IntensityTranslationOptions)
translator.register(Duration, DurationTranslationOptions)
