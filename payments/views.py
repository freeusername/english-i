# -*- coding: utf-8 -*-
import datetime
import urlparse
import logging
from decimal import Decimal
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from liqpay.integration import LiqPayIntegration
from liqpay import models as lp_models

from payments.utils import order2json, get_order, get_password, FraudAttemptError
from payments.crypto import encrypt

from . import models
from core.configs.models import AppConfig

logger = logging.getLogger('app')
ORDER_ID = 'ORDER_PK'

