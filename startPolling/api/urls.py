from startPolling.api import views
from django.urls import path 
from rest_framework import routers 

app_name = 'startPolling'

urlpatterns = [
    path('question/', views.questions_view, name='question_view'), 
    path('question/<int:question_id>/', views.question_detail_view, name='question_detail_view'),
    # path('social_sign_up/', views.SocialSignUp.as_view(), name="social_sign_up"),
    # path('question/<int:question_id>/choices/', views.choices_view, name='choices_view'),
    # path('question/<int:question_id>/result/', views.question_result_view, name='question_result_view'), 
    path('question/<int:question_id>/comment/', views.comments_view, name='comments_view'), 
    # path('question/<int:question_id>/vote/', views.vote_view, name='vote_view'),
    
]