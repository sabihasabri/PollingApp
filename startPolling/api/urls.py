from startPolling.api.views import QuestionView, QuestionDetailView
from django.urls import path 
from rest_framework import routers 

urlpatterns = [
    path('questions/', QuestionView, name='question_view'), 
    path('<int:id>/', QuestionDetailView)
]