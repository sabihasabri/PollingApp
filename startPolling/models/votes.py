from django.db import models
from .questions import Question 
from .choices import Choice
import datetime
from django.conf import settings
from django.contrib.auth.models import User


class Vote(models.Model): 
    Votes = models.IntegerField(default=0)
    ChoiceId = models.ForeignKey(Choice, related_name = 'votes', on_delete=models.CASCADE)
    QuestionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    IP =  models.GenericIPAddressField()
    

    