from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    avatar_url = models.URLField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    @property
    def avatar_img_url(self):
        return "" + self.avatar_url

    def __str__(self):
        return self.user.first_name