import re
from django.template import Library
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

MONTHS = {
    1: _('January'), 2: _('February'), 3: _('March'), 4: _('April'), 5: _('May'), 6: _('June'),
    7: _('July'), 8: _('August'), 9: _('September'), 10: _('October'), 11: _('November'),
    12: _('December')
}

register = Library()

@register.filter
def normalize_text(value):
    return re.sub(r'(?<=[\.,:!\?])(?![\.,:!\?\s])', ' ', value)


@register.filter
def format(value, arg):
    """
    Alters default filter "stringformat" to not add the % at the front,
    so the variable can be placed anywhere in the string.
    """
    try:
        if value:
            return (unicode(arg)) % value
        else:
            return u''
    except (ValueError, TypeError):
        return u''

@register.filter
def copyright_year(start_year):
    start_year = int(start_year)
    year = timezone.now().year
    if year > start_year:
        return "%s - %s" % (start_year, year)
    return year

@register.filter
def date_var_format(date):
    result = ""
    if date:
        current_date = timezone.now()
        short_form = (date.year == current_date.year)
        if short_form:
            result = u"%s %s" % (date.day, MONTHS[date.month])
        else:
            result = u"%s %s %s" % (date.day, MONTHS[date.month], date.year)
    return result



