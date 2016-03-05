# -*- coding: utf-8 -*-
from functools import wraps
from django.core.exceptions import PermissionDenied
import simplejson as json
import urllib
from django.http import HttpResponse


class JsonResponse(HttpResponse):

    def __init__(self, content=b'', *args, **kwargs):
        kwargs['content_type'] = 'application/json'
        content = json.dumps(content)
        super(JsonResponse, self).__init__(content, *args, **kwargs)


def urldecode(query):
    data = {}
    array = query.split('&')
    for string in array:
        if string.find('='):
            key, value = map(urllib.unquote, string.split('='))
            try:
                data[key].append(value)
            except KeyError:
                data[key] = [value]

    return data


def require_ajax(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        request = args[0]

        if not request.is_ajax():
            raise PermissionDenied

        return view(*args, **kwargs)

    return wrapper
