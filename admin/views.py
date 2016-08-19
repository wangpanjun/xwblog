# coding=utf-8

from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import get_user


class SysView(View):

    def post(self, request):
        pass
        # print get_user(request)
        # return HttpResponse()

    def delete(self, request):
        pass
