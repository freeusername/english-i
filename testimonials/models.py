from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models.fields import ImageSpecField
from core.utils.helpers import get_file_path
from pilkit.processors import ResizeToFit, ResizeToFill
from uuslug import uuslug

# Create your models here.


class Testimonial(models.Model):
    show = models.BooleanField(_('show?'), default=True)
    position = models.PositiveIntegerField(_('position'), default=0)
    title = models.CharField(_('title'), max_length=27, default='')
    link = models.URLField(_('link'), null=True, blank=True)
    description = models.TextField(_('description'), null=True, blank=True)
    full_name = models.CharField(_('full name'), max_length=255, null=True, blank=True)
    info = models.CharField(_('info'), max_length=255, null=True, blank=True)
    image = models.ImageField(_('image'), upload_to=get_file_path, null=True)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    admin_thumb = ImageSpecField([ResizeToFit(height=60, upscale=False)], source='image')
    image_thumb = ImageSpecField([ResizeToFill(width=79, height=79, upscale=False)], source='image')

    def __unicode__(self):
        return self.title

    @property
    def upload_dir(self):
        return "testimonials/images"

    def admin_thumbnail(self):
        if self.image:
            return '<img src="{}" />'.format(self.admin_thumb.url)
        else:
            return ''
    admin_thumbnail.short_description = _('image')
    admin_thumbnail.allow_tags = True

    class Meta:
        ordering = ['position']
        verbose_name = _('testimonial')
        verbose_name_plural = _('testimonials')


class Teacher(models.Model):
    show = models.BooleanField(_('show?'), default=True)
    position = models.PositiveIntegerField(_('position'), default=0)
    full_name = models.CharField(_('full name'), max_length=255, default='')
    # link = models.URLField(_('link'), null=True, blank=True)
    description = models.TextField(_('description'), null=True, blank=True)
    # full_name = models.CharField(_('full name'), max_length=255, null=True, blank=True)
    # info = models.CharField(_('info'), max_length=255, null=True, blank=True)
    image = models.ImageField(_('image'), upload_to=get_file_path, null=True)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    admin_thumb = ImageSpecField([ResizeToFit(height=60, upscale=False)], source='image')
    image_thumb = ImageSpecField([ResizeToFill(width=274, height=292, upscale=False)], source='image')

    def __unicode__(self):
        return self.full_name

    @property
    def upload_dir(self):
        return "teachers/images"

    def admin_thumbnail(self):
        if self.image:
            return '<img src="{}" />'.format(self.admin_thumb.url)
        else:
            return ''
    admin_thumbnail.short_description = _('image')
    admin_thumbnail.allow_tags = True

    class Meta:
        ordering = ['position']
        verbose_name = _('teacher')
        verbose_name_plural = _('teachers')