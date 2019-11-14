from startPolling.models import Question 
from django.http import HttpResponse
from datetime import datetime 
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets 
from .serializers import QuestionSerializer
from rest_framework import generics 
from rest_framework.decorators import api_view

# @csrf_exempt
# def question_view(request):
#     if request.method == 'GET': 
#         return HttpResponse("Not Implemented yet")
#     elif request.method == 'POST':
#         question_text = request.POST['question_text']
#         pub_date = datetime.strptime(request.POST['pub_date'], '%Y-%m-%d')
#         created_by = request.POST['user']
#         description = request.POST['description']
#         Question.objects.create(question_text=question_text, pub_date=pub_date, created_by=user, description=description)
#         return HttpResponse("Question created", status=201)


class QuestionView(viewsets.ModelViewSet): 
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = (IsCreatedByOrReadOnly)

    def perform_create(self, serializer): 
        serializer.save(created_by=self.request.user)

class QuestionDetailView(generics.ListAPIView): 
    queryset =Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

class ChoiceView(viewsets.ModelViewSet): 
    @api_view(['POST'])
    def choices_view(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        serializer = ChoiceSerializer(data=request.data, many=True)
        if serializer.is_valid():
            choice = serializer.save(question=question)
            return Response(ChoiceSerializer(choice).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)