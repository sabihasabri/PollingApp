from django.db import models
from .questions import Question 

class Choice(models.Model): 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text =  models.CharField(max_length=200)
    
    def __str__(self): 
        return self.choice_text 

    # @property
    # def choiceproperty(self): 
    #     return self.question.choiceproperty.id