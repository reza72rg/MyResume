from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    def clean_username(self):
            username = self.cleaned_data.get('username')
            user = User.objects.filter(username=username).exists()
            if user:
                raise ValidationError('This username already exists',code="username_exists")
            return username.strip() 
        
    def clean_email(self):
            email = self.cleaned_data.get('email')
            user = User.objects.filter(email=email).exists()
            if user:
                raise ValidationError('This email already exists',code="email_exists")
            return email.strip() 
      
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        



    