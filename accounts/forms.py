from django import forms 
from .models import Register 


class UserForm(forms.models): 
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta: 
        model = UserForm
        fields = (
            'name', 
            'email', 
            'password', 
            'password-again',
        )