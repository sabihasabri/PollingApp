from django.db import models
from .questions import Question 
from .choices import Choice
import datetime
from django.conf import settings
# from django.contrib.auth import get_user_model 
from django.contrib.auth.models import User


class Vote(models.Model): 
    votes = models.IntegerField(default=0)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta: 
        unique_together = ("question", "voted_by")