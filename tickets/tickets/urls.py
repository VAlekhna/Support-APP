from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from support.views import AnswerViewSet, QuestionViewSet

router = SimpleRouter()

router.register(r'question', QuestionViewSet)
router.register(r'answer', AnswerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += router.urls
