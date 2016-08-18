# encoding=utf-8

from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseNotFound
import json

from questions.models import DoQuestion

class QuestionsView(View):

    def post(self, request):
        pass

    def get(self, request):
        pass


class QuestionView(View):

    def get(self, request, question_id):
        info = DoQuestion.get_by_id(question_id)
        if info:
            return HttpResponse(json.dumps(json))
        return HttpResponseNotFound()

    def delete(self, request, request_id):
        DoQuestion.delete_by_id(request_id)
        return HttpResponse()

    def put(self, request):
        pass
