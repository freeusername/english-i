# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class ConfigsConfig(AppConfig):
    name = 'core.configs'
    verbose_name = _('Configs')


