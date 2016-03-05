from django.db import models
from django.utils.translation import ugettext_lazy as _

from imagekit.models.fields import ImageSpecField
from core.utils.helpers import get_file_path
from pilkit.processors import ResizeToFit, ResizeToFill


class Slide(models.Model):
    show = models.BooleanField(_('show?'), default=True)
    position = models.PositiveIntegerField(_('position'), default=0)
    top_text = models.TextField(_('top text'), blank=True, null=True)
    bottom_text = models.TextField(_('bottom text'), blank=True, null=True)
    image = models.ImageField(_('slide'), upload_to=get_file_path)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    admin_thumb = ImageSpecField([ResizeToFit(height=60, upscale=False)], source='image')
    main_slide = ImageSpecField([ResizeToFill(width=1000, height=517, upscale=False)], source='image')

    def __unicode__(self):
        return u"Slide #%s" % self.pk

    @property
    def upload_dir(self):
        return "slides/images"

    def admin_thumbnail(self):
        if self.image:
            return '<img src="{}" />'.format(self.admin_thumb.url)
        else:
            return ''
    admin_thumbnail.short_description = _('image')
    admin_thumbnail.allow_tags = True

    class Meta:
        ordering = ['position']
        verbose_name = _('slide')
        verbose_name_plural = _('slides')