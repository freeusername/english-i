# -*- coding: utf-8 -*-
import os
import uuid
import datetime
import smtplib
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage
from djlime.utils import mail
from . import logger

def clean_sting(s):
    import re
    return re.sub("^\s+|\n|\r|\s+$", '', s)

def send_mail(recipients=None, subject_template='', html_template=None,
              text_template=None, context=None, **kwargs):
    try:
        mail.send_mail(
            recipients=recipients,
            subject_template=subject_template,
            html_template=html_template,
            text_template=text_template,
            context=context,
            kwargs=kwargs
        )
    except smtplib.SMTPException as e:
        err_msg = e.message
        logger.error("An error occured while sending the email:")
        logger.error(u"  %s" % err_msg)
        return False
    else:
        return True


def parts_of(thelist, n, fill_with=None):
    result = []
    length = len(thelist)
    i = 0
    while i < length:
        row = [fill_with]*n
        j = 0
        while i<length and j<n:
            row[j] = thelist[i]
            i += 1
            j += 1
        result.append(row)
    return result


def group_of(list, number, fill_with=None):
    result = []
    _len = len(list)
    _division = _len / number
    _modulo = _len % number
    _start = 0
    for index in range(0, number):
        _length = _division + (1 if (_modulo > 0 and _modulo > index) else 0)
        _padding = (1 if (fill_with and _modulo > 0 and _length == _division) else 0)
        _end = _start + _length
        result.append(list[_start:_end]+([fill_with] * _padding))
        _start = _end
    return result


def show_more_factory(request, objects, per_page, num_pages_param='num_pages'):
    num_pages = int(request.GET.get(num_pages_param, "1"))
    v__per_page = num_pages*per_page
    paginator = Paginator(objects, v__per_page)

    try:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    return objects, num_pages


def date_to_begin_day(date):
    return datetime.datetime(date.year, date.month, date.day, tzinfo=timezone.get_current_timezone())


def date_to_end_day(date):
    return datetime.datetime(date.year, date.month, date.day,
        hour=23, minute=59, second=59, microsecond=999999,
        tzinfo=timezone.get_current_timezone())


def generate_dates_range(start_date, end_date):
    return [(start_date + datetime.timedelta(n))
            for n in range(1, (end_date - start_date).days + 1)]

def get_file_path(obj, filename):
   if hasattr(obj, 'upload_dir'):
       extension = filename.split('.')[-1]
       filename = "%s.%s" % (uuid.uuid4(), extension)
       return os.path.join(obj.upload_dir, filename)
   else:
       raise AttributeError("%s does not have 'upload_dir' attribute" % obj.__class__.__name__)

def get_pdf_path(obj, filename):
   if hasattr(obj, 'upload_dir_pdf'):
       extension = filename.split('.')[-1]
       filename = "%s.%s" % (uuid.uuid4(), extension)
       return os.path.join(obj.upload_dir_pdf, filename)
   else:
       raise AttributeError("%s does not have 'upload_dir_pdf' attribute" % obj.__class__.__name__)

def get_grammatical_case(sum, unit_nominative, unit_genitive, unit_accusative):
    if 11 <= sum <= 14:
        return u"%s %s" % (sum, unit_accusative)
    import math
    num = int(math.fmod(sum, 10))
    if num == 1:
        return u"%s %s" % (sum, unit_nominative)
    elif 2 <= num <= 4:
        return u"%s %s" % (sum, unit_genitive)
    else:
        return u"%s %s" % (sum, unit_accusative)