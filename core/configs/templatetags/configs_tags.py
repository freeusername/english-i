# -*- coding: utf-8 -*-
from django.template import Library, TemplateSyntaxError, Node
from ..models import AppConfig

register = Library()


@register.tag
def get_config(parser, token):
    tokens = token.split_contents()

    if len(tokens) < 2:
        raise TemplateSyntaxError("'%s' takes at least one argument (path to a view)" % tokens[0])

    key_name = parser.compile_filter(tokens[1])
    asvar = None
    tokens = tokens[2:]
    if len(tokens) >= 2 and tokens[-2] == 'as':
        asvar = tokens[-1]
    return configNode(key_name, asvar)


class configNode(Node):
    def __init__(self, key_name, asvar):
        self.key_name = key_name
        self.asvar = asvar

    def render(self, context):
        result = ""
        config = None
        key_name = self.key_name.resolve(context)

        try:
            config = AppConfig.objects.get(key=key_name, enabled=True)
        except AppConfig.DoesNotExist:
            pass

        if config:
            result = config.value

        if self.asvar:
            context[self.asvar] = result
            result = ""
        return result
