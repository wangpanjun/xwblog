# encoding=utf-8

from django.views.generic.base import View

from django.shortcuts import render


def index(request):
    context = {}
    template = "index.html"
    return render(request, template, context)
