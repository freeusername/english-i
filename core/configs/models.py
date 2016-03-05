# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

CFG_TYPE_BOOLEAN = 'boolean'
CFG_TYPE_INTEGER = 'integer'
CFG_TYPE_FLOAT = 'float'
CFG_TYPE_DECIMAL = 'decimal'
CFG_TYPE_LINK = 'link'
CFG_TYPE_DATE = 'date'
CFG_TYPE_DATETIME = 'datetime'
CFG_TYPE_STRING = 'string'
CFG_TYPE_STRING_ML = 'string_ml'
CFG_TYPE_TEXT = 'text'
CFG_TYPE_TEXT_ML = 'text_ml'
CFG_TYPE_HTML = 'html'
CFG_TYPE_HTML_ML = 'html_ml'

CFG_TYPES = (
    (CFG_TYPE_BOOLEAN, _('Boolean')),
    (CFG_TYPE_INTEGER, _('Integer')),
    (CFG_TYPE_FLOAT, _('Float')),
    (CFG_TYPE_DECIMAL, _('Decimal')),
    (CFG_TYPE_LINK, _('Link')),
    (CFG_TYPE_DATE, _('Date')),
    (CFG_TYPE_DATETIME, _('DateTime')),
    (CFG_TYPE_STRING, _('String')),
    (CFG_TYPE_STRING_ML, _('String multilangual')),
    (CFG_TYPE_TEXT, _('Text')),
    (CFG_TYPE_TEXT_ML, _('Text multilanguall')),
    (CFG_TYPE_HTML, _('Html')),
   (CFG_TYPE_HTML_ML, _('Html multilanguall')),
)


class AppConfig(models.Model):
    key = models.CharField(_('key'), max_length=255)
    enabled = models.BooleanField(_('enabled?'), default=True)
    value_type = models.CharField(_('type'), max_length=25, default=CFG_TYPE_BOOLEAN, choices=sorted(list(CFG_TYPES), key=lambda ct: ct[1]))
    value_name = models.CharField(_('name'), max_length=255)
    # -- value types --
    value_boolean = models.NullBooleanField(_('value'), blank=True, null=True)
    value_integer = models.IntegerField(_('value'), blank=True, null=True)
    value_float = models.FloatField(_('value'), blank=True, null=True)
    value_decimal = models.DecimalField(_('value'), blank=True, null=True, decimal_places=2, max_digits=20)
    value_link = models.URLField(_('value'), blank=True, null=True)
    value_date = models.DateField(_('value'), blank=True, null=True)
    value_datetime = models.DateTimeField(_('value'), blank=True, null=True)
    value_string = models.CharField(_('value'), max_length=255, blank=True, null=True)
    value_string_ml = models.CharField(_('value'), max_length=255, blank=True, null=True)
    value_text = models.TextField(_('value'), blank=True, null=True)
    value_text_ml = models.TextField(_('value'), blank=True, null=True)
    value_html = HTMLField(_('value'), blank=True, null=True)
    value_html_ml = HTMLField(_('value'), blank=True, null=True)
    # -- end value types --
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __unicode__(self):
        return self.value_name

    @property
    def value(self):
        return getattr(self, u'value_%s' % self.value_type)

    class Meta:
        db_table = 'app_configs'
        ordering = ['key']
        verbose_name = _('app config')
        verbose_name_plural = _('app configs')
