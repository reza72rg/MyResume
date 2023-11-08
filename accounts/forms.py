from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    def clean_email(self):
            email = self.cleaned_data['email']
            user = User.objects.filter(email=email).exists()
            if user:
                raise ValidationError('this email already exists')
            return email 
        
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        



    