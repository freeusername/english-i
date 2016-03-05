from django.contrib import admin
from django.db import models
from imagekit.admin import AdminThumbnail
from core.utils.widgets import AdminFileThumbWidget
from core.metatags.admin import MetaTagInline
from modeltranslation.admin import TabbedTranslationAdmin, TranslationAdmin, TranslationTabularInline
from core.utils import TranslationTabsMixin
from tinymce.widgets import TinyMCE
from django.forms import CheckboxSelectMultiple
import courses.translation

from .models import Course, Skill, Intensity, Duration


class DurationInline(TranslationTabularInline):
    model = Duration
    fk_name = "intensity"
    extra = 0
    readonly_fields = ('full_price',)


class SkillAdmin(TabbedTranslationAdmin):
    list_display = ('position', 'title', 'lessons')
    list_display_links = ('title',)
    list_editable = ('position',)
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    inlines = [MetaTagInline]


class CourseAdmin(TranslationAdmin, TranslationTabsMixin):
    list_display = ('title', 'value_type', 'user')
    list_display_links = ('title',)
    list_filter = ('value_type', 'user')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        # models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    filter_horizontal = ('skills',)
    fieldsets = (
        (None, {'fields': ('value_type', 'title',)}),
        (None, {
            'classes': ('cls-course_front value_fields',),
            'fields': ('position', 'featured', 'skill', 'slug', 'short_description', 'description', 'lessons',
                       'duration', 'pros_cons', 'price', 'preview', 'image'),
        }),
        (None, {
            'classes': ('cls-course_personal value_fields',),
            'fields': ('user', 'skills', 'no_skills',),
        }),
    )
    inlines = [MetaTagInline]

    class Media:
        js = (
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
            '/static/courses/admin/js/configs_support.js',
        )
        # js.append('/static/modeltranslation/js/force_jquery.js')
        # js.append('http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js')
        # js.append('/static/modeltranslation/js/tabbed_translation_fields.js')
        # js.append('/static/configs/admin/js/configs_support.js')
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }


class IntensityAdmin(TabbedTranslationAdmin):
    list_display = ('position', 'title', 'recommended')
    list_display_links = ('title',)
    list_editable = ('position', 'recommended')
    formfield_overrides = {}
    inlines = [DurationInline]

#
# class PersonalCourseAdmin(TabbedTranslationAdmin):
#     list_display = ('__unicode__', 'position',)
#     list_display_links = ('__unicode__',)
#     list_editable = ('position',)
#     formfield_overrides = {}


admin.site.register(Course, CourseAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Intensity, IntensityAdmin)
# admin.site.register(PersonalCourse, PersonalCourseAdmin)
