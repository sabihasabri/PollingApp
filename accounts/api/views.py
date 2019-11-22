# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from accounts.api.serializers import RegistrationSerializer, UserSerializer

# @api_view(['POST'])
# def registration_view(request):
#     if request.method == 'POST': 
#         serializer = RegistrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid(): 
#             account = serializer.save()
#             data['response'] = 'successfully registered a new user'
#             data['email'] = account.email
#             data['username'] = account.username
#         else: 
#             data  = serializer.errors
#         return Response(data)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.api.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 
from rest_framework.permissions import IsAuthenticated, AllowAny



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.api.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 
from rest_framework.permissions import IsAuthenticated, AllowAny



class UserCreate(APIView):
    """ 
    Creates the user. 
    """
    look_up = "pk"
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # generating tokens for the user
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                print(token)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class Logout(APIView): 
    def get(self, request, format=None): 
        #simply delete the token to force a login 
       
        print(Token.objects.get(user=request.user))
        Token.objects.get(user=request.user).delete()

        
        return Response(status=status.HTTP_200_OK)