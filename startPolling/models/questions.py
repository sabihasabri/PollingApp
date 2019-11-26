from django.db import models
import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.reverse import reverse as api_reverse 


class Question(models.Model): 
    QuestionText = models.CharField(max_length=500, blank=False, null=False)
    Description = models.TextField(blank=True)
    # CreatedBy = models.ForeignKey(User, null=True, blank=True, related_name = 'CreatedBy', on_delete=models.CASCADE)
    CreationDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    IsAllowComments = models.BooleanField(null=True, help_text = 'Allow comments on user submissions.')
    IsPrivate = models.BooleanField(default=False)
    IsMultiple= models.BooleanField(default=False)
    # EndDate = models.DateTimeField(null=True, blank=True)
    
    def RecentlyAdded(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.CreationDate <= now

    def choices(self):
        if not hasattr(self, '_choices'):
            self._choices = self.choice_set.all()
        return self._choices

    def comments(self):
        if not hasattr(self, '_comments'):
            self._comments = self.comment_set.all()
        return self._comments

    # def get_api_url(self, request=None): 
    #     return api_reverse('api-polls:detail_view', request=request)


    def __str__(self): 
        return self.QuestionText