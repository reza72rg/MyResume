from django import forms
from blog.models import Comment
from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm): 
    captcha = CaptchaField() 
    def clean_subject(self):
        return ''
    
    class Meta:
        model = Comment
        fields = ['name','email','subject','message']