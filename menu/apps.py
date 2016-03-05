from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ItemConfig(AppConfig):
    name = 'menu'
    verbose_name = _('Site menu')
