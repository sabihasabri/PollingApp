from rest_framework import serializers
from startPolling.models import Question, Choice, Comment
from django.utils import timezone




class CommentSerializer(serializers.Serializer): 
    id = serializers.IntegerField(read_only=True)
    CommentField = serializers.CharField(max_length=5000)
   
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

class ChoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    choice_text = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)


# class QuestionSerializer(serializers.Serializer): 
#     QuestionText = serializers.CharField()
#     id = serializers.IntegerField()
#     Description = serializers.CharField(max_length=500)
#     IsAllowComments = serializers.BooleanField(default=False, help_text = 'Allow comments on user submissions.')
#     IsPrivate = serializers.BooleanField(default=False)
#     IsMultiple= serializers.BooleanField(default=False)
#     RecentlyAdded = serializers.BooleanField(read_only=True)
#     url =  serializers.SerializerMethodField(read_only=True)
#     choices = ChoiceSerializer(many=True, read_only=True)
#     comments = CommentSerializer(many=True)

#     def create(self, validated_data):
#         return Question.objects.create(**validated_data)
    
    
    
#     def update(self, instance, validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()
#         return instance
      
#     def get_url(self, obj): 
#         #request
#         request = self.context.get("request")
#         return obj.get_api_url(request=request)
class QuestionListPageSerializer(serializers.Serializer):
    id              = serializers.IntegerField(read_only=True)
    QuestionText    = serializers.CharField()
    Description     = serializers.CharField(max_length=500)
    IsAllowComments = serializers.BooleanField(default=False, help_text = 'Allow comments on user submissions.')
    IsPrivate       = serializers.BooleanField(default=False)
    IsMultiple      = serializers.BooleanField(default=False)
    RecentlyAdded   = serializers.BooleanField(read_only=True)
    url             = serializers.SerializerMethodField(read_only=True)
    choices         = ChoiceSerializer(many=True, write_only=True)
    comment         = CommentSerializer(many=True, write_only=True)

    
    # comments= serializers.SerializerMethodField()
    
    # class Meta:
    #      model = Poll
    #      fields = ('name','details','comments')
    # def get_comments(self,obj):
    #      poll_comment = FluentComment.objects.filter(object_pk = obj.id, parent_id = None)
    #      serializer = CommentSerializer(poll_comment,many=True)
    #      return serializer.data
    
    def create(self, validated_data):
        choices = validated_data.pop('choices', [])
        question = Question.objects.create(**validated_data)
        for choice_dict in choices:
            choice_dict['question'] = question
            Choice.objects.create(**choice_dict)
        return question

    
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
   
    def get_url(self, obj): 
        #request
        request = self.context.get("request")
        return obj.get_api_url(request=request)

class QuestionDetailPageSerializer(QuestionListPageSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    comment = CommentSerializer(many=True, read_only=True)


class VoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()

class ChoiceSerializerWithVotes(ChoiceSerializer):
    votes = serializers.IntegerField(read_only=True)

class QuestionResultSerializer(QuestionListPageSerializer):
    choices = ChoiceSerializerWithVotes(many=True, read_only=True)
# class RecursiveField(serializers.Serializer):
#     def to_representation(self, value):
#         serializer = self.parent.parent.__class__(
#             value,
#             context=self.context)
#         return serializer.data

# class CommentSerializer(serializers.ModelSerializer):
#     children = RecursiveField(many=True)
    
#     class Meta:
#         model = FluentComment
#         fields = (
#             'comment',
#             'id',
#             'children',
#            )






    

