from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from startPolling.models import Question, Choice
from .serializers import QuestionListPageSerializer, QuestionDetailPageSerializer, ChoiceSerializer, CommentSerializer

@api_view(['GET', 'POST'])
def questions_view(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionListPageSerializer(questions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionListPageSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionListPageSerializer(question).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def question_detail_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'GET':
        serializer = QuestionDetailPageSerializer(question)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = QuestionDetailPageSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionDetailPageSerializer(question).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        question.delete()
        return Response("Question deleted", status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def choices_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    serializer = ChoiceSerializer(data=request.data)
    if serializer.is_valid():
        choice = serializer.save(question=question)
        return Response(ChoiceSerializer(choice).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def comments_view(request, question_id):
    QID = get_object_or_404(Question, pk=question_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        choice = serializer.save(QID=QID)
        return Response(CommentSerializer(choice).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PATCH'])
# def vote_view(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     serializer = VoteSerializer(data=request.data)
#     if serializer.is_valid():
#         choice = get_object_or_404(Choice, pk=serializer.validated_data['choice_id'], question=question)
#         choice.votes += 1
#         choice.save()
#         return Response("Voted")
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def question_result_view(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     serializer = QuestionResultPageSerializer(question)
#     return Response(serializer.data)

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = FluentComment.objects.all()
#     serializer_class = CommentSerializer
#     def create(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             data = self.request.data
#             comment = data['comment']
#             poll = data['Question']
#             if 'parent' in data:
#                 parent = data['parent']
#             else:
#                 parent = None
#             submit_date = datetime.now()
#             content = ContentType.objects.get(model="Question").pk
#             comment = FluentComment.objects.create(object_pk=poll, comment=comment, submit_date=submit_date,   content_type_id=content,user_id = self.request.user.id, site_id=settings.SITE_ID, parent_id=parent)
#             serializer = CommentSerializer(comment,context=  {'request': request})
#             return Response(serializer.data)