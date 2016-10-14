# coding=utf=-8

from django.views.generic.base import View

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from helper.helper import validate_form, result_json
from forms import ArticleForm, ArticlePageForm
from models import DoArticle
from django.shortcuts import render

from helper.pagination import Pager
import json


class ArticlesView(View):
    def get(self, request):
        flag, data = validate_form(ArticlePageForm, request.GET)

        if not flag:
            return HttpResponseBadRequest(json.dumps(data))
        page_num = data.get('page_num', 1)
        page_size = data.get('page_size', 10)
        info = DoArticle.get_by_page(page_num, page_size, data)
        pager = Pager(len(info), page_num, page_size)
        template = "article-list.html"
        return render(request, template, {"data": info, "pager": pager.render_page_tag()})

    def post(self, request):
        pass


class ArticleView(View):
    def get(self, request, article_id):
        info = DoArticle.get_by_id(article_id)
        template = "article_detail.html"
        return render(request, template, info)
