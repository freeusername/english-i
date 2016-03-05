from django.contrib import admin
from django.db import models
from imagekit.admin import AdminThumbnail
from core.utils.widgets import AdminFileThumbWidget
from core.metatags.admin import MetaTagInline
from modeltranslation.admin import TabbedTranslationAdmin
from tinymce.widgets import TinyMCE
import testimonials.translation
from .models import Testimonial, Teacher

class TestimonialAdmin(TabbedTranslationAdmin):
    list_display = ('admin_thumbnail', 'show', 'position', 'title', 'full_name')
    list_display_links = ('title', 'full_name', 'admin_thumbnail')
    list_editable = ('position', 'show',)
    formfield_overrides = {
        models.ImageField: {'widget': AdminFileThumbWidget()},
        # models.TextField: {'widget': TinyMCE()},
    }


class TeacherAdmin(TabbedTranslationAdmin):
    list_display = ('admin_thumbnail', 'show', 'position', 'full_name')
    list_display_links = ('full_name', 'admin_thumbnail')
    list_editable = ('position', 'show',)
    formfield_overrides = {
        models.ImageField: {'widget': AdminFileThumbWidget()},
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Teacher, TeacherAdmin)