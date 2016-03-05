from django.template import Library
from django.utils import translation
from django.utils.encoding import force_unicode

from core.metatags.models import MetaTag


register = Library()

_get_page_title = lambda page_object, page_title_field: (
    getattr(page_object, page_title_field, force_unicode(page_object))
)


@register.inclusion_tag('metatags/meta_tags.html', takes_context=True)
def include_meta_tags(context, page_object=None, page_title_field='title',
                      default_title=''):
    if page_object is not None:
        # Get the meta tags for the object
        try:
            meta_tags = MetaTag.objects \
                .get(object_id=page_object.id,
                     content_type__app_label=page_object._meta.app_label)
            # Get not blank title
            meta_tags.title = meta_tags.title or \
                _get_page_title(page_object, page_title_field)
        except MetaTag.DoesNotExist:
            meta_tags = {
                'title': _get_page_title(page_object, page_title_field)
            }
    else:
        try:
            # Get the meta tags for the URL-path
            url = context['request'].path_info

            if not url.startswith('/'):
                url = "/" + url

            language = translation.get_language()
            language_prefix = '/%s' % language

            if url.startswith(language_prefix):
                url = url[len(language_prefix):]

            meta_tags = MetaTag.objects.get(url=url)
            meta_tags.title = meta_tags.title or default_title
        except (KeyError, MetaTag.DoesNotExist):
            meta_tags = {
                'title': default_title,
                'keywords': '',
                'description': ''
            }
    return {'meta_tags': meta_tags}
