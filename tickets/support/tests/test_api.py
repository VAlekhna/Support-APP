import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


from support.models import Question
from support.serializers import QuestionSerializer


class QuestionsApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username')
        self.question_1 = Question.objects.create(name='Vopros', text='Spasiti')
        self.question_2 = Question.objects.create(name='Vopros2', text='Pamagiti2')
        self.question_3 = Question.objects.create(name='Vopros3', text='Pamagiti3', question_status='Рассмотрено')
        self.question_4 = Question.objects.create(name='Spasiti', text='Pamagiti4', question_status='Приостановлено')

    def test_get(self):
        url = reverse('question-list')
        response = self.client.get(url)
        serializer_data = QuestionSerializer([self.question_1, self.question_2, self.question_3, self.question_4],
                                             many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('question-list')
        response = self.client.get(url, data={'search': 'Spasiti'})
        serializer_data = QuestionSerializer([self.question_1, self.question_4], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self,):
        url = reverse('question-list')
        data = {
            "name": "POST TEST",
            "text": "Does the POST request work?"
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')

        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

