from django.contrib import admin

# Register your models here.
from labels.models import LabelModel

admin.site.register(LabelModel)