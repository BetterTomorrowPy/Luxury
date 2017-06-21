# -*- coding: utf-8 -*-
""""""

from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class TestView(View):

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(TestView, self).dispatch(request, *args, **kwargs)
    @method_decorator(login_required)
    def get(self, request):
        return JsonResponse({
            'code': 0,
            'msg': 'Logined user.'
        })