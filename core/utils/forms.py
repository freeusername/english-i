# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _


class AdminFileThumbWidget(AdminFileWidget):
    """
    A AdminFileWidget that shows a delete checkbox
    """
    input_type = 'file'

    def render(self, name, value, attrs=None):
        input = super(forms.widgets.FileInput, self).render(name, value, attrs)
        if value:
            item = '<tr><td style="vertical-align: middle;">%s</td><td>%s</td>'
            output = []
            preview_image = value
            output.append('<table style="border-style: none;">')
            output.append(item % (_('Currently: '), '<a target="_blank" href="%s%s">%s</a>' % (settings.MEDIA_URL, value, value)))
            output.append(item % (_('Preview: '), '<img src="%s%s" height="100" />' % (settings.MEDIA_URL, preview_image)))
            output.append(item % (_('Change: '), input))
            output.append('</table>')
            return mark_safe(u''.join(output))
        else:
            return mark_safe(input)


class TabularInlineImageWidget(forms.FileInput):
    """
    A ImageField Widget for admin that shows a thumbnail.
    """

    def __init__(self, attrs={}):
        super(TabularInlineImageWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            output.append(('<a target="_blank" href="%s">'
                           '<img src="%s" style="height: 50px;" /></a> '
                           % (value.url, value.url)))
        output.append(super(TabularInlineImageWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
