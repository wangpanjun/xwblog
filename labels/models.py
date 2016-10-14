from django.db import models


class LabelModel(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=32)
    from_user = models.CharField(max_length=64, null=True)
    to_user = models.CharField(max_length=64, null=True)
    created_time = models.DateField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    flag = models.BooleanField(default=True)

    class Meta:
        db_table = 'label'
