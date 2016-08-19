# coding=utf-8

from articles.models import ArticleModel, CategoryModel
import unittest


class ArticleModelTest(unittest.TestCase):
    def setUp(self):
        self.category = {
            'name': "python"
        }
        category = CategoryModel.objects.create(**self.category)
        self.article = dict(
            title='python',
            content='python ~~',
            category=category
        )

        article = ArticleModel.objects.create(**self.article)
        print category
        # article.category = category
        # article.save()

    def test_get_by_id(self):
        pass

    def tearDown(self):
        ArticleModel.objects.all().delete()
