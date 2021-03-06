from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from .models import MetaTag


class InlineMetaTagForm(forms.ModelForm):

    class Meta:
        model = MetaTag
        fields = ('title', 'keywords', 'description')
        widgets = {
            'title': forms.TextInput({'class': 'meta_title'}),
            'keywords': forms.TextInput({'class': 'meta_keywords'}),
            'description': forms.Textarea({'class': 'meta_description'})
        }

    class Media:
        css = {
            'all': ('css/meta_tags.css',)
        }


class MetaTagForm(InlineMetaTagForm):
    url = forms.RegexField(label=_('URL-path'), max_length=255, regex=r'^[-\w/\.~]+$',
                           help_text=_("Example: '/about/contact/'. Make sure to have leading "
                                       "and trailing slashes."),
                           error_message=_("This value must contain only letters, numbers,"
                                           "dots, underscores, dashes, slashes or tildes."),
                           widget=forms.TextInput({'class': 'meta_title'}))

    class Meta(InlineMetaTagForm.Meta):
        fields = ('url', 'title', 'keywords', 'description')

    class Media:
        css = {
            'all': ('css/meta_tags.css',)
        }

    def clean_url(self):
        url = self.cleaned_data['url']

        if not url.startswith('/'):
            raise forms.ValidationError(_('URL is missing a leading slash.'))

        if (settings.APPEND_SLASH and
            'django.middleware.common.CommonMiddleware' in settings.MIDDLEWARE_CLASSES and
            not url.endswith('/')):
            raise forms.ValidationError(_('URL is missing a trailing slash.'))

        if MetaTag.objects.filter(url=url).exists():
            if self.instance is None:
                raise forms.ValidationError(_('Meta-tags for a given URL-path have already been identified.'))
            elif url != self.instance.url:
                raise forms.ValidationError(_('Meta-tags for a given URL-path have already been identified.'))

        return url
