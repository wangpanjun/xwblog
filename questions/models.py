# ~~~ coding=utf-8 @xiaowang~~~

from django.db import models
from django.utils import timezone


class TagModel(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=62)
    created_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tag'

    def detail(self):
        return {
            "name": self.name,
            "tag_id": self.tag_id
        }


class AnswerModel(models.Model):
    answer_id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField(auto_now=True)
    answer = models.TextField(null=True)
    detail = models.TextField(null=True)

    class Meta:
        db_table = 'answer'

    def info(self):
        return {
            "answer_id": self.answer_id,
            "answer": self.answer,
            "detail": self.detail,
            "created_time": self.created_time
        }


# 问题
class QuestionModel(models.Model):
    question_id = models.AutoField(primary_key=True)
    # user_id = models.AutoField()
    title = models.CharField(max_length=512, null=True, db_index=True)
    tags = models.ManyToManyField(TagModel, blank=True)
    created_time = models.DateTimeField(auto_now=True)
    answers = models.ManyToManyField(AnswerModel, blank=True)

    class Meta:
        db_table = 'question'

    def detail(self):
        return {
            "question_id": self.question_id,
            "title": self.title,
            "created_time": self.created_time,
            "tag": [tag.detail() for tag in self.tags.all()],
        }

    def info(self):
        return {
            "question_id": self.question_id,
            "title": self.title,
            "created_time": self.created_time,
            "tags": [tag.detail() for tag in self.tags.all()],
            "answers": [answer.info() for answer in self.answers.all()]
        }


class DoQuestion(object):
    @staticmethod
    def get_by_page(condition):
        page_num = condition.get("page_num", 1)
        page_size = condition.get("page_size", 10)
        title = condition.get("title", None)
        questions = QuestionModel.objects.all()
        if title:
            questions = questions.filter(title__contains=title)
        return [question.detail() for question in questions[(page_num - 1) * page_size, page_size]]

    @staticmethod
    def get_by_id(id):
        try:
            return QuestionModel.objects.get(question_id=id).info()
        except QuestionModel.DoesNotExist:
            pass

    @staticmethod
    def delete_by_id(id):
        try:
            QuestionModel.objects.get(question_id=id).delete()
        except QuestionModel.DoesNotExist:
            pass

    @staticmethod
    def save(param):
        tags = param.get("tags", "")
        tags_obj = TagModel.objects.filter(tag_id__int=tags)
        param.pop("tags")
        question = QuestionModel.objects.create(**param)
        question.tags = tags_obj
        question.save()
