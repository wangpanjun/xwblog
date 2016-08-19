# coding-utf-8

from django.conf.urls import  url
from views import ArticlesView, ArticleView

urlpatterns = [
    url(r'^articles$', ArticlesView.as_view()),
    url(r'^article/(\d+)$', ArticleView.as_view()),
]

