from django.contrib import admin
from django.contrib.admin import ModelAdmin

from support.models import Question, Answer


admin.site.register(Question)
admin.site.register(Answer)
# @admin.register(Question)
# class QuestionAdmin(ModelAdmin):
#     pass

