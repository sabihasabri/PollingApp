from rest_framework import serializers
from accounts.models import Account 
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

# class RegistrationSerializer(serializers.ModelSerializer): 
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
#     class Meta: 
#         model = Account
#         fields = ['name', 'email', 'password', 'password2']
#         extra_kwargs = {
#             'password': {'write_only' : True}
#         }

#     def save(self): 
#         account = Account(
#             email=self.validated_data['email'], 
#             username=self.validated_data['username'], 
#         )

#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']

#         if password!= password-again: 
#             raise serializers.ValidationError({'password': 'password not match.'})
#         account.set_password(password)
#         account.save()
#         return account


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators = [UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators = [UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)


    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
            validated_data['password'])
        return user

    class Meta:
        model = Account
        fields = ('id', 'username', 'email', 'password')