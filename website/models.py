from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.models.fields.files import ImageFieldFile
from PIL import Image
from io import BytesIO
from django.core.files import File
from mysite.tools import UploadToPathAndRename


def get_image_field(self):
    output = []
    for k, v in self.__dict__.items():
        if isinstance(v, ImageFieldFile):
            output.append(k)
    return output


class MainModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=_("create date"))
    modify_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name=_("modify date"))
    is_active = models.BooleanField(default=True, verbose_name=_("is active"))

    def save(self, *args, **kwargs):
        image_fields = get_image_field(self)
        if image_fields:
            for i in image_fields:
                if hasattr(self, i) and isinstance(getattr(self, i), ImageFieldFile):
                    image = Image.open(getattr(self, i).file)
                    image_io = BytesIO()
                    image_extension = getattr(self, i).name.rpartition(".")[-1].upper()
                    image_extension = "JPEG" if image_extension == "JPG" else image_extension
                    image.save(image_io, image_extension, quality=60)
                    new_image = File(image_io, name=getattr(self, i).name)
                    setattr(self, i, new_image)
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class NewsLetter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email

class Information(MainModel):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to=UploadToPathAndRename("website"),default='website/defualt.jpg')
    job = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100,null=True)
    website = models.CharField(max_length=100)
    birthday = models.DateField()
    age = models.PositiveIntegerField(default=0)
    degree = models.CharField(max_length=50)
    freelance = models.CharField(max_length=50)
    about_me= models.TextField()
    my_works = models.CharField(max_length=255,null=True) 
    
    def __str__(self):
        return str(self.author)


class Skill(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.TextField()
    def __str__(self):
        return str(self.author)
     
class My_Skill(models.Model):
    author = models.ForeignKey(Skill,on_delete=models.SET_NULL,null=True)
    skill = models.CharField(max_length=20)
    percent = models.PositiveIntegerField(default=0)
    def __str__(self):
        return str(self.author)
    
    
    
class UserImage(MainModel):
    username = models.ForeignKey(Information, on_delete=models.CASCADE)
    image_more = models.ImageField(upload_to=UploadToPathAndRename("website"),default='website/defualt.jpg')


