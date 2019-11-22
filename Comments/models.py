from django.db import models

class Comment(models.Model):
    CommentField = models.CharField(max_length=5000, blank=True, null=True)
    QID = models.ForeignKey(Question, on_delete= models.CASCADE) 
    Parent = models.ForeignKey("self", null=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
