# coding~~utf-8

from django.db import models
from questions.models import TagModel

from django.utils import timezone


class CategoryModel(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    created_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'

    def detail(self):
        return dict(category_id=self.category_id, name=self.name)


class ArticleModel(models.Model):
    article_id = models.AutoField(primary_key=True)
    tags = models.ManyToManyField(TagModel)
    category = models.ForeignKey(CategoryModel)
    title = models.CharField(max_length=256)
    content = models.TextField(blank=True)
    views = models.IntegerField(default=0)
    images = models.CharField(max_length=256, blank=True)
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'article'

    def detail(self):
        return dict(
            article_id=self.article_id,
            title=self.title,
            views=self.views,
            content=self.content,
            created_time=self.created_time,
            category=self.category.name,
            tags=[tag.detail() for tag in self.tags.all()]
        )

    def info(self):
        return dict(
            article_id=self.article_id,
            title=self.title,
            views=self.views,
            created_time=self.created_time,
            category=self.category.name,
            tags=[tag.detail() for tag in self.tags.all()]
        )


class DoArticle(object):
    @staticmethod
    def get_by_id(id):
        try:
            article = ArticleModel.objects.get(article_id=id)
            return article.detail()
        except ArticleModel.DoesNotExist:
            return None

    @staticmethod
    def get_by_page(page_num, page_size, param):
        title = param.get('title', '')
        articles = ArticleModel.objects.filter(title__contains=title).order_by('-created_time')[
                   (page_num - 1) * page_size:page_size]
        return [article.info() for article in articles]

    @staticmethod
    def save(parm):
        pass

    @staticmethod
    def delete(id):
        pass
