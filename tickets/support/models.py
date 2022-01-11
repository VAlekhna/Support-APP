from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    class StatusChoice(models.TextChoices):
        reviewed = 'Рассмотрено', 'Рассмотрено'
        under_consideration = 'На рассмотрении', 'На рассмотрении'
        suspended = 'Приостановлено', 'Приостановлено'

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор вопроса', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Суть вопроса')
    text = models.TextField(verbose_name='Ваш вопрос')
    question_status = models.CharField(max_length=20, choices=StatusChoice.choices, default='На рассмотрении',
                                       blank=True, null=True)
    parent = models.ForeignKey('self', verbose_name='Первоначальный вопрос', blank=True, null=True,
                               related_name='answer_children', on_delete=models.CASCADE)

    def __str__(self):
        return f'Id{self.id}: {self.name} - {self.question_status}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос',
                                 blank=False, null=True, related_name='answer_questions')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор ответа', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Текст ответа')

    def __str__(self):
        return f'Id{self.id}: {self.author}'
