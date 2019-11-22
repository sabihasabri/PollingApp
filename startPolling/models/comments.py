from django.db import models
from .questions import Question 


class Comment(models.Model): 
    QID = models.ForeignKey('Question', on_delete=models.CASCADE)
    CommentField = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.CommentField