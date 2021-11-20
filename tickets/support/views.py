from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from support.models import Question
from support.serializers import QuestionSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    filter_fields = ['question_status']
    search_fields = ['name', 'text']
    ordering_fields = ['question_status', 'create_date']

    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()
