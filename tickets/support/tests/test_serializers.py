
from django.test import TestCase

from support.models import Question
from support.serializers import QuestionSerializer


# class QuestionSerializerTestCase(TestCase):
#     def test_ok(self):
#         question_1 = Question.objects.create(name='Vopros', text='Spasiti')
#         question_2 = Question.objects.create(name='Vopros2', text='Spasiti2')
#         data = QuestionSerializer([question_1, question_2], many=True).data
#         expected_data = [
#             {
#                 'name': 'Vopros',
#                 'text': 'Spasiti'
#             },
#             {
#                 'name': 'Vopros2',
#                 'text': 'Spasiti2'
#             },
#         ]
#         self.assertEqual(expected_data, data)
