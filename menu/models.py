# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from imagekit.models.fields import ImageSpecField
from core.utils.helpers import get_file_path
from pilkit.processors import ResizeToFit, ResizeToFill

# MENU_LOCATION_TOP = 'top'
# MENU_LOCATION_BOTTOM = 'bottom'
#
# MENU_LOCATION_VALUES = (
#     (MENU_LOCATION_TOP, _('Top menu')),
#     (MENU_LOCATION_BOTTOM, _('Bottom menu')),
# )

_('Menu')


# LOCATION_CHOICES = (
#     ('top', _('top menu')),
#     ('bottom', _('bottom menu')),
# )


@python_2_unicode_compatible
class Item(models.Model):
    # location = models.CharField(verbose_name=_('location'), max_length=255, choices=LOCATION_CHOICES)
    title = models.CharField(verbose_name=_('name'), max_length=255, default='')
    position = models.PositiveIntegerField(verbose_name=_('position'), default=0,)

    link = models.CharField(verbose_name=_('url'), max_length=255, blank=True, default='',
                            help_text=_('example: /about/'))
    search_template = models.CharField(_('search template'), blank=True, max_length=255, default='^{}')

    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True)
    
    def __str__(self):
        return self.title

    # def get_subitems(self):
    #     return Subitem.objects.filter(item=self)
    
    class Meta:
        ordering = ['position']
        verbose_name = _('item')
        verbose_name_plural = _('items')


# @python_2_unicode_compatible
# class Subitem(models.Model):
#     item = models.ForeignKey(Item, verbose_name=_('item'), related_name='menu_subitem')
#     title = models.CharField(verbose_name=_('name'), max_length=255, default='')
#     position = models.PositiveIntegerField(verbose_name=_('position'), default=0,)
#     link = models.CharField(verbose_name=_('url'), max_length=255, default='', help_text=_('example: /about/'))
#
#     created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
#     updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         ordering = ['position']
#         verbose_name = _('subitem')
#         verbose_name_plural = _('subitems')