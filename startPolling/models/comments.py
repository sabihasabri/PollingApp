from django.db import models 
from .questions import Question

class Comment(models.Model): 
    text = models.TextField(blank=True, null=True)
    comment = models.ForeignKey(Question, on_delete=models.CASCADE)