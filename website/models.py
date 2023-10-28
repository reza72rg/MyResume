from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class NewsLetter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email
    