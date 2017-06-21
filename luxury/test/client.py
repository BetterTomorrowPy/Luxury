# -*- coding: utf-8 -*-
"""
    Django test client. RequestFactory, Client
"""
from __future__ import unicode_literals

import re

from io import BytesIO

from django.conf import settings
from django.http import SimpleCookie
from django.utils import six
from django.core.handlers.wsgi import WSGIRequest, ISO_8859_1

BOUNDARY = 'BoUnDaRyStRiNg'
MULTIPART_CONTENT = 'multipart/form-data; boundary=%s' % BOUNDARY
CONTENT_TYPE_RE = re.compile(r'.*; charset=([\w\d-]+);?')
JSON_CONTENT_TYPE_RE = re.compile(r'^application\/(vnd\..+\+)?json')


class RedirectCycleError(Exception):
    """"""

    def __init__(self, message, last_response):
        super(RedirectCycleError, self).__init__(message)
        self.last_response = last_response
        self.redirect_chain = last_response.redirect_chain


class FakePayload(object):
    pass


def encode_multipart():
    pass


def force_bytes():
    pass


class RequestFactory(object):
    """
    usage:

        rf = RequestFactory()
        get_request = rf.get('/hello/')
        post_request = rf.post('/submit/', {'headers': headers})
    """

    def __init__(self, **defaults):
        self.defaults = defaults
        self.cookies = SimpleCookie()
        self.errors = BytesIO()

    def _base_environ(self, **request):
        """
        set environment for request
        """
        environ = {
            'HTTP_COOKIE': self.cookies.output(header='', sep='; '),
            'PATH_INFO': str('/'),
            'REMOTE_ADDR': str('127.0.0.1'),
            'REQUEST_METHOD': str('GET'),
            'SCRIPT_NAME': str(''),
            'SERVER_NAME': str('testserver'),
            'SERVER_PORT': str('80'),
            'SERVER_PROTOCOL': str('HTTP/1.1'),
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': str('http'),
            'wsgi.input': FakePayload(b''),
            'wsgi.errors': self.errors,
            'wsgi.multiprocess': True,
            'wsgi.multithread': False,
            'wsgi.run_once': False,
        }
        environ.update(self.defaults)
        environ.update(request)
        return environ

    def request(self, **request):
        """构造通用请求对象"""
        return WSGIRequest(self._base_environ(**request))

    def _encode_data(self, data, content_type):
        if content_type is MULTIPART_CONTENT:
            return encode_multipart(BOUNDARY, data)
        else:
            match = CONTENT_TYPE_RE.match(content_type)
            if match:
                charset = match.group(1)
            else:
                charset = settings.DEFAULT_CHARSET
            return force_bytes(data, encoding=charset)

    def _get_path(self, parsed):
        path = force_str(parsed[2])
        if parsed[3]:
            path += str(';') + force_str(parsed[3])
        path = uri_to_iri(path).encode(UTF_8)
        return path.decode(ISO_8859_1) if six.PY3 else path
