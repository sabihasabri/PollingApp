from django.db import models
import datetime
from django.conf import settings
from django.contrib.auth.models import User


class Question(models.Model): 
    question_text = models.CharField(max_length=500)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('created on')
    description = models.TextField(blank=True)
    # starts_at = models.DateTimeField(default=datetime.datetime.now)
    # ends_at = models.DateTimeField(null=True, blank=True)
    # allow_comments = models.BooleanField(default=False, help_text = 'Allow comments on user submissions.')
    # is_private = models.BooleanField(default=False)
    # allow_multiple= models.BooleanField(default=False)


    def __str__(self): 
        return self.question_text