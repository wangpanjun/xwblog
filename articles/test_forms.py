# coding=utf-8


import unittest

from forms import ArticleForm


class ArticleFormTest(unittest.TestCase):
    def setUp(self):
        data = [
            ({"tags": "12,3"}, False),
            ({"tags": "1,2,4", "category": 1, "title": "11"}, False)
        ]
        for dat, flag in data:
            form = ArticleForm(dat)
            rst = form.is_valid()
            self.assertEqual(rst, flag)

    def test_valid(self):
        pass

    def tearDown(self):
        pass
