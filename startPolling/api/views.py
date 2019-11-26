from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.contrib.auth.models import User 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from startPolling.models import Question, Choice
from .serializers import QuestionListPageSerializer, UserSerializer, QuestionDetailPageSerializer, ChoiceSerializer
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
import requests
from rest_framework.views import APIView
from rest_framework import generics 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated





class GetDetails(generics.ListAPIView): 
    permission_classes = [IsAuthenticated,]
    queryset = Question.objects.all()
    serializer_class = QuestionListPageSerializer



@api_view(['POST'])
def create_poll(request): 
    if request.method == 'POST':
        serializer = QuestionListPageSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionListPageSerializer(question).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class DeleteQuestion(APIView):
#     permission_classes = [IsAuthenticated,]
#     def delete(self, request, pk, format=None):
#         question = self.get_object(pk)
#         question.delete()
#         return Response("Question deleted", status=status.HTTP_204_NO_CONTENT)


@api_view(['PATCH'])
# @permission_classes((IsOwnerOrReadOnly,))
def edit_question(request, question_id): 
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'PATCH': 
        serializer = QuestionDetailPageSerializer(question)
        return Response(serializer.data)
    else: 
        return Response("Wrong Choice")



@api_view(['DELETE'])
def delete_view(request, question_id): 
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'DELETE': 
        question.delete()
        return Response("Question deleted", status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def detail_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'GET': 
        serializer = QuestionDetailPageSerializer(question)
        return Response(serializer.data)






# @api_view(['GET', 'PATCH', 'DELETE'])
# def question_detail_view(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     if request.method == 'GET':
#         serializer = QuestionDetailPageSerializer(question)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         serializer = QuestionDetailPageSerializer(question, data=request.data, partial=True)
#         if serializer.is_valid():
#             question = serializer.save()
#             return Response(QuestionDetailPageSerializer(question).data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         question.delete()
#         return Response("Question deleted", status=status.HTTP_204_NO_CONTENT)





@api_view(['POST'])
def choices_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    serializer = ChoiceSerializer(data=request.data)
    if serializer.is_valid():
        choice = serializer.save(question=question)
        return Response(ChoiceSerializer(choice).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListAPIView): 
    permission_classes= [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrentUser(generics.RetrieveAPIView): 
    def get(self, request): 
        serializer = UserSerializer(request.user)
        return Response(serializer.data)



class GoogleView(APIView):
    def post(self, request):
        payload = {'access_token': request.data.get("token")}  # validate the token
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)

        # create user if not exist
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            user = User()
            user.username = data['email']
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.save()

        token = RefreshToken.for_user(user)  # generate token without username & password
        response = {}
        response['username'] = user.username
        response['access_token'] = str(token.access_token)
        response['refresh_token'] = str(token)
        return Response(response)
