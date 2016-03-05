from __future__ import absolute_import, unicode_literals

from itertools import chain

from django.forms.widgets import CheckboxInput, RadioSelect, FileInput
from django.forms.widgets import SelectMultiple, Select
from django.contrib.admin.widgets import AdminFileWidget
from django.forms.util import flatatt
from django.utils.html import conditional_escape, format_html, format_html_join
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from django.conf import settings

#from treebeard.models import Node

#def formated_choices(iterator):
#    field = iterator.field
#    choices = []
#    if field:
#        if field.required:
#            pass
#        else:
#            if field.empty_label is None:
#                pass
#            else:
#                choices = [[None, field.empty_label]]
#    qs = iterator.queryset
#    if qs:
#        model = qs.model
#        if issubclass(model, Node):
#            root_nodes = model.get_root_nodes()
#            for root_node in root_nodes:
#                children = [[n.pk, n.name] for n in root_node.get_children()]
#                if children:
#                    choices.append([root_node.name, children])
#    return choices
#
#class TreeAsGroupedSelect(Select):
#
#    def render_options(self, choices, selected_choices):
#        # Normalize to strings.
#        selected_choices = set(force_text(v) for v in selected_choices)
#        output = []
#        for option_value, option_label in chain(formated_choices(self.choices), choices):
#            if isinstance(option_label, (list, tuple)):
#                output.append(format_html('<optgroup label="{0}">', force_text(option_value)))
#                for option in option_label:
#                    output.append(self.render_option(selected_choices, *option))
#                output.append('</optgroup>')
#            else:
#                output.append(self.render_option(selected_choices, option_value, option_label))
#        return '\n'.join(output)
#
#class TreeAsGroupedSelectMultiple(SelectMultiple):
#
#    def render_options(self, choices, selected_choices):
#        # Normalize to strings.
#        selected_choices = set(force_text(v) for v in selected_choices)
#        output = []
#        for option_value, option_label in chain(formated_choices(self.choices), choices):
#            if isinstance(option_label, (list, tuple)):
#                output.append(format_html('<optgroup label="{0}">', force_text(option_value)))
#                for option in option_label:
#                    output.append(self.render_option(selected_choices, *option))
#                output.append('</optgroup>')
#            else:
#                output.append(self.render_option(selected_choices, option_value, option_label))
#        return '\n'.join(output)


class AdminFileThumbWidget(AdminFileWidget):
    """
    A AdminFileWidget that shows a delete checkbox
    """
    input_type = 'file'

    def render(self, name, value, attrs=None):
        input = super(FileInput, self).render(name, value, attrs)
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


class TabularInlineImageWidget(FileInput):
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


# class CurrencyRadioSelect(RadioSelect):
#
#     def render(self, name, value, attrs=None, choices=()):
#         output = []
#         for i, (option_value, option_label) in enumerate(chain(self.choices, choices)):
#             # If an ID attribute was given, add a numeric index as a suffix,
#             # so that the checkboxes don't all have the same ID attribute.
#             if option_value == "":
#                 # skip empty values
#                 pass
#             else:
#                 final_attrs = self.build_attrs(attrs, name=name)
#                 option_value = force_text(option_value)
#                 rb = RadioInput(name, value, final_attrs, (option_value, option_label,), i)
#                 rendered_rb = rb.tag()
#                 label_for = format_html(' for="{0}"', final_attrs['id'])
#                 option_label = force_text(option_label)
#                 output.append(format_html('<label{1}>{0} <span class="radio_label">{2}</span></label>',
#                     rendered_rb, label_for, option_label))
#         return mark_safe('\n'.join(output))


class BrandsSelectMultiple(SelectMultiple):

    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = []
        has_id = attrs and 'id' in attrs
        final_attrs = self.build_attrs(attrs, name=name)
        output = []
        # Normalize to strings
        str_values = set([force_text(v) for v in value])
        for i, (option_value, option_label) in enumerate(chain(self.choices, choices)):
            # If an ID attribute was given, add a numeric index as a suffix,
            # so that the checkboxes don't all have the same ID attribute.
            if has_id:
                final_attrs = dict(final_attrs, id='%s_%s' % (attrs['id'], i))
                label_for = format_html(' for="{0}"', final_attrs['id'])
            else:
                final_attrs['id'] = '%s_%s' % (self.attrs['id'], i)
                label_for = format_html(' for="{0}"', final_attrs['id'])

            cb = CheckboxInput(final_attrs, check_test=lambda value: value in str_values)
            option_value = force_text(option_value)
            rendered_cb = cb.render(name, option_value)
            option_label = force_text(option_label)
            output.append(format_html('<label{0} class=\'brand\'>\n<span class=\'label\'>{1}</span>\n{2}\n</label>',
                label_for, option_label, rendered_cb))
        return mark_safe('\n'.join(output))
