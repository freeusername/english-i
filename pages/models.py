# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce import models as tinymce_models

class Page(models.Model):
    url = models.CharField(_('url'), max_length=255, default='', help_text=_("Example: '/about/'. Make sure to have "
                                                                             "leading and trailing slashes."))
    title = models.CharField(_('title'), max_length=255, default='')
    show_title = models.BooleanField(_('show title?'), default=True)
    enabled = models.BooleanField(_('enabled?'), default=True)
    content = tinymce_models.HTMLField(_('content'), blank=True, default='')
    template = models.CharField(_('template'), max_length=255, blank=True, default='', help_text=_('Example: about, '
                                                                                                   'if not filled will '
                                                                                                   'use the default '
                                                                                                   'template.'))

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.url

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')
