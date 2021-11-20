from django.contrib import admin
from django.contrib.admin import ModelAdmin

from support.models import Question


# admin.site.register(Question)

@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    pass

