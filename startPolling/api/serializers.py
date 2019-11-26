from rest_framework import serializers
from startPolling.models import Question, Choice, Comment
from django.utils import timezone



class ChoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    choice_text = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)


class ChoiceSerializerWithVotes(ChoiceSerializer):
    votes = serializers.IntegerField(read_only=True)


class QuestionListPageSerializer(serializers.Serializer):
    id              = serializers.IntegerField(read_only=True)
    QuestionText    = serializers.CharField()
    # CreatedBy = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    Description     = serializers.CharField(max_length=500)
    IsAllowComments = serializers.BooleanField(default=False, help_text = 'Allow comments on user submissions.')
    IsPrivate       = serializers.BooleanField(default=False)
    IsMultiple      = serializers.BooleanField(default=False)
    RecentlyAdded   = serializers.BooleanField(read_only=True)
    # url             = serializers.SerializerMethodField(read_only=True)
    choices         = ChoiceSerializer(many=True, write_only=True)
    # comment         = CommentSerializer(many=True, write_only=True)

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
   
    # def get_url(self, obj): 
    #     request = self.context.get("request")
    #     return obj.get_api_url(request=request)


class QuestionDetailPageSerializer(QuestionListPageSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)


class QuestionResultPageSerializer(QuestionListPageSerializer):
    choices = ChoiceSerializerWithVotes(many=True, read_only=True)
    max_voted_choice = ChoiceSerializerWithVotes(read_only=True)


class VoteSerializer(serializers.Serializer):
    choice_id = serializers.IntegerField()


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

class UserSerializer(serializers.Serializer):
    id  = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)






# class QuestionListPageSerializer(serializers.Serializer):
#     id              = serializers.IntegerField(read_only=True)
#     QuestionText    = serializers.CharField()
#     Description     = serializers.CharField(max_length=500)
#     IsAllowComments = serializers.BooleanField(default=False, help_text = 'Allow comments on user submissions.')
#     IsPrivate       = serializers.BooleanField(default=False)
#     IsMultiple      = serializers.BooleanField(default=False)
#     RecentlyAdded   = serializers.BooleanField(read_only=True)
#     url             = serializers.SerializerMethodField(read_only=True)
#     choices         = ChoiceSerializer(many=True, write_only=True)
#     # comment         = CommentSerializer(many=True, write_only=True)

    
#     # comments= serializers.SerializerMethodField()
    
#     # class Meta:
#     #      model = Poll
#     #      fields = ('name','details','comments')
#     # def get_comments(self,obj):
#     #      poll_comment = FluentComment.objects.filter(object_pk = obj.id, parent_id = None)
#     #      serializer = CommentSerializer(poll_comment,many=True)
#     #      return serializer.data
    
#     def create(self, validated_data):
#         choices = validated_data.pop('choices', [])
#         question = Question.objects.create(**validated_data)
#         for choice_dict in choices:
#             choice_dict['question'] = question
#             Choice.objects.create(**choice_dict)
#         return question

    
    
#     def update(self, instance, validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()
#         return instance
   
#     def get_url(self, obj): 
#         #request
#         request = self.context.get("request")
#         return obj.get_api_url(request=request)

# class QuestionDetailPageSerializer(QuestionListPageSerializer):
#     choices = ChoiceSerializer(many=True, read_only=True)
#     # comment = CommentSerializer(many=True, read_only=True)


# class VoteSerializer(serializers.Serializer):
#     choice_id = serializers.IntegerField()

# class ChoiceSerializerWithVotes(ChoiceSerializer):
#     votes = serializers.IntegerField(read_only=True)

# class QuestionResultSerializer(QuestionListPageSerializer):
#     choices = ChoiceSerializerWithVotes(many=True, read_only=True)






    

