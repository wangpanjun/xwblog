# coding=utf=-8

from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from helper.helper import validate_form
from forms import ArticleForm, ArticlePageForm
from models import DoArticle
from django.shortcuts import render

import json


class ArticlesView(View):
    def get(self, request):
        flag, data = validate_form(ArticlePageForm, request.GET)
        if not flag:
            return HttpResponseBadRequest(json.dumps(data))
        info = DoArticle.get_by_page(data)
        # template = "article_list.html"
        content = {"data":info}
        template = "article_list.html"
        return render(request, template, content)

    def post(self, request):
        pass


class ArticleView(View):
    def get(self, request, article_id):
        info = DoArticle.get_by_id(article_id)
        template = "article_detail.html"
        return render(request, template, info)
