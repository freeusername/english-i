from django.contrib import admin
from django.db import models
from imagekit.admin import AdminThumbnail
from core.utils.widgets import AdminFileThumbWidget
from modeltranslation.admin import TabbedTranslationAdmin
from tinymce.widgets import TinyMCE
import slides.translation
from .models import Slide


class SlideAdmin(TabbedTranslationAdmin):
    list_display = ('admin_thumbnail', 'position', 'show',)
    list_display_links = ('admin_thumbnail',)
    list_editable = ('position', 'show',)
    formfield_overrides = {
        models.ImageField: {'widget': AdminFileThumbWidget()},
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(Slide, SlideAdmin)