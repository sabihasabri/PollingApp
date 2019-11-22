from django.contrib.auth.models import User
from rest_framework import generics, permissions

class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserSerializer