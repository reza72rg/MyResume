from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileUser(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE )
    image = models.ImageField(upload_to='blog/%y/%m/%d/',default='blog/defualt.jpg') 
    age = models.PositiveSmallIntegerField(default=0)
    job = models.CharField(max_length=200)
