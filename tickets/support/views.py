from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from support.models import Answer, Question
from support.permissions import IsStaffOrQuestionOnly, IsStaffOrReadOnly
from support.serializers import AnswerSerializer, QuestionSerializer
from .tasks import send_alert


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsStaffOrQuestionOnly]
    filter_fields = ['question_status']
    search_fields = ['name', 'text']
    ordering_fields = ['question_status', 'create_date']

    def perform_create(self, serializer):
        send_alert.delay()
        serializer.validated_data['author'] = self.request.user
        serializer.save()


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsStaffOrReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()
