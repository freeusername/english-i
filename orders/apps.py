from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class OrderConfig(AppConfig):
    name = 'orders'
    verbose_name = _('Orders')