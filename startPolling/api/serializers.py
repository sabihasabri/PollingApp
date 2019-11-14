from rest_framework import serializers
from startPolling.models import Question 
from startPolling.models import Choice 


class QuestionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Question 
        fields = (
            'id', 
            'question_text', 
            'created_by', 
            'pub_date', 
            'description', 
            # 'start_at', 
            # 'ends_at', 
            # 'allow_comment', 
            # 'is_private', 
            # 'allow_multiple', 
        )
        extra_kwargs = {'created_by': {'default':serializers.CurrentUserDefault()}}

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    
    def validate_question_text(self, value): 
        qs = Question.objects.filter(title__iexact=value)
        if self.instance: 
            qs = qs.exclude(pk=self.instance.id)

        if qs.exists(): 
            raise serailizers.ValidationError('question_text is available')
        return value


class ChoiceSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Choice 
        fields = (
            'choices'
        )

    def create(self,validated_data): 
        return Choice.objects.create(**validated_data)
