# -*- coding: utf-8 -*-
"""
    工具系列
"""
import json
import logging
import functools

from voluptuous import MultipleInvalid
from django.http import JsonResponse
from django.utils import six


class ApiBadRequest(JsonResponse):
    status_code = 400

    def __init__(self, *args, **kwargs):
        super(ApiBadRequest, self).__init__(*args, **kwargs)


def schema_validator(schema):
    """
    :param schema: voluptuous.Schema
    :return:
    """

    def func_wrapper(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            content_type = self.request.content_type
            if content_type and content_type.startswith('application/json'):
                body = self.request.body
                if six.PY3:
                    body = body.decode('utf-8')
                _arguments = json.loads(body)
            else:
                _arguments = dict()
                if 'GET' == self.request.method:
                    _arguments = self.request.GET.dict()
                elif 'POST' == self.request.method:
                    _arguments = self.request.POST.dict()

            try:
                self.request.json_arguments = schema(_arguments)
            except MultipleInvalid as e:
                error_message = 'path: {0} message: {1}' \
                    .format(e.path, e.error_message)
                logging.debug(error_message)
                return ApiBadRequest(data={'code': -1, 'msg': error_message})
            return method(self, *args, **kwargs)

        return wrapper

    return func_wrapper
