from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from support.models import Question, Answer
from support.permissions import IsStaffOrReadOnly
from support.serializers import QuestionSerializer, AnswerSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsStaffOrReadOnly]
    filter_fields = ['question_status']
    search_fields = ['name', 'text']
    ordering_fields = ['question_status', 'create_date']

    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()

