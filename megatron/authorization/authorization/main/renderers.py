from __future__ import unicode_literals
from django.utils import six
from rest_framework.compat import (
    INDENT_SEPARATORS, LONG_SEPARATORS, SHORT_SEPARATORS
)
from rest_framework.utils import json
from rest_framework.renderers import JSONRenderer


class MyJSONRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):

        if data is None:
            return bytes()

        renderer_context = renderer_context or {}
        response = renderer_context['response']
        indent = self.get_indent(accepted_media_type, renderer_context)

        if indent is None:
            separators = SHORT_SEPARATORS if self.compact else LONG_SEPARATORS
        else:
            separators = INDENT_SEPARATORS

        # My added part

        if response.exception:
            status = "error {}".format(response.status_code)
            response_dict = {'status': status, 'message': data.get('detail')}
        else:
            status = "success"
            response_dict = {'status': status, 'data': data}

        data = response_dict

        # End of my added part

        ret = json.dumps(
            data, cls=self.encoder_class,
            indent=indent, ensure_ascii=self.ensure_ascii,
            allow_nan=not self.strict, separators=separators
        )

        if isinstance(ret, six.text_type):
            ret = ret.replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
            return bytes(ret.encode('utf-8'))
        return ret

