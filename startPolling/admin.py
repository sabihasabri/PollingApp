from django.contrib import admin
from .models import Question
from .models import Choice 
from .models import Vote
from .models import Comment

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Vote)
admin.site.register(Comment)



