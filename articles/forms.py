# coding=utf-8

from django import forms


class ArticleForm(forms.Form):
    tags = forms.CharField(max_length=128)
    category = forms.IntegerField(min_value=1)
    title = forms.CharField(min_length=1, max_length=64)
    content = forms.CharField(min_length=1)
    images = forms.FileField()


class ArticlePageForm(forms.Form):
    page_num = forms.IntegerField(min_value=1, required=False)
    page_size = forms.IntegerField(min_value=10, max_value=30, required=False)
    title = forms.CharField(max_length=50, required=False)

    def clean(self):
        if not self.cleaned_data.get('page_num'):
            self.cleaned_data['page_num'] = 1

        if not self.cleaned_data.get('page_size'):
            self.cleaned_data['page_size'] = 10

        return self.cleaned_data
