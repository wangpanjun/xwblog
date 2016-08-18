# coding=utf-8

from django.conf.urls import patterns, url
from views import QuestionsView, QuestionView

urlpatterns = patterns(
    '',
    url(r'^questions$', QuestionsView.as_view()),
    url(r'^question(\d*)$', QuestionView.as_view()),
    url(r'^questions$', QuestionsView.as_view()),
)

