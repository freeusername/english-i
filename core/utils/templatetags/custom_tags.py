# -*- coding: utf-8 -*-
import re
from django.template import Library
from django.utils.translation import ugettext as _
from django.core.urlresolvers import resolve, reverse, Resolver404
from django.utils.translation import activate, get_language
from django.conf import settings

register = Library()

#@register.simple_tag(takes_context=True)
@register.simple_tag
def change_lang(request, lang=None, *args, **kwargs):
    """
    Get active page's url by a specified language
    Usage: {% change_lang 'en' %}
    """
    path = request.path
    if not path.startswith('/'):
        path = "/" + path
    url_parts = None
    try:
        url_parts = resolve( path )
    except Resolver404:
        pass
    url = path
    cur_language = get_language()
    if url_parts:
        try:
            activate(lang)
            url = reverse( url_parts.view_name, kwargs=url_parts.kwargs )
        finally:
            activate(cur_language)
    else:
        language_prefix = '/%s' % cur_language
        if url.startswith(language_prefix):
            cleaned_url = url[len(language_prefix):]
            url = '/%s%s' % (lang, cleaned_url)
    return "%s" % url


@register.simple_tag
def is_curr_link(request, link, format='^{}', css_class='active'):
    url = request.path
    if not url.startswith('/'):
        url = "/" + url
    pattern = format.format(link)

    language = request.LANGUAGE_CODE
    language_prefix = '/%s' % language

    if url.startswith(language_prefix):
        url = url[len(language_prefix):]
    if re.search(pattern, url):
        return css_class
    return ''


@register.simple_tag
def lang_selector(request):
    cur_lang_code = get_language()
    cur_lang_name = ''
    other_langs = []
    for k, v in settings.LANGUAGES:
        if k == cur_lang_code:
            cur_lang_name = _(v)
        else:
            other_langs.append([k,_(v)])
    result = u"""
        <div class="now uppercase">
            <span>%s:</span>
            %s
        </div>
    """ % (_('LANGUAGE'), cur_lang_name)
    result += u"<ul>\n"
    for ll in other_langs:
        form_name = u"setLang_%s" % ll[0]
        result += u"    <li><a href=\"javascript:void(0);\" onclick=\"document.%s.submit();return false;\">%s</a></li>\n" % (form_name, ll[1])
    result += u"</ul>\n"
    return result

@register.simple_tag
def lang_prefix_for_menu():
    result = ''
    cur_lang = get_language()
    default_lang = settings.LANGUAGE_CODE
    if cur_lang == default_lang:
        pass
    else:
        result = '/%s' % cur_lang
    return result