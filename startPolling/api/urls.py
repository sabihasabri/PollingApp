from startPolling.api import views
from django.urls import path 


app_name = 'startPolling'

urlpatterns = [
    path('questions/', views.GetDetails.as_view(), name='get_detials'), 
    path('question/', views.create_poll, name='create_poll'),   
    path('question/<int:question_id>/', views.detail_view, name='detail_view'),  
    path('question/<int:question_id>/edit/', views.edit_question, name='edit'),
    path('question/<int:question_id>/delete/', views.delete_view, name='delete'),  
    path('validate/', views.GoogleView, name= "validateToken"),
    path('me/', views.CurrentUser.as_view(), name="CurrentUser"),
    path('users/', views.UserList.as_view(), name="UserList"), 
    # path('questions/', views.DeleteQuestion.as_view(), name='deleteQuestion'),
    # path('questions/', views.get_details, name='get_detials'), 
    # path('question/<int:question_id>/choices/', views.choices_view, name='choices_view'),
    # path('question/<int:question_id>/result/', views.question_result_view, name='question_result_view'), 
    # path('question/<int:question_id>/comment/', views.comments_view, name='comments_view'), 
    # path('question/<int:question_id>/vote/', views.vote_view, name='vote_view'),
    # path('question/', views.questions_view, name='questions_view'),  
    
]