from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.models.fields.files import ImageFieldFile
from PIL import Image
from io import BytesIO
from django.core.files import File
from mysite.tools import UploadToPathAndRename
from datetime import date


class MainModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=_("create date"))
    modify_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name=_("modify date"))
    is_active = models.BooleanField(default=True, verbose_name=_("is active"))

    def get_image_fields(self):
        return [k for k, v in self.__dict__.items() if isinstance(v, ImageFieldFile)]

    def save(self, *args, **kwargs):
        image_fields = self.get_image_fields()
        if image_fields:
            for field_name in image_fields:
                image_field = getattr(self, field_name)
                if isinstance(image_field, ImageFieldFile) and image_field:
                    image = Image.open(image_field.file)
                    image_io = BytesIO()
                    image_extension = image_field.name.rpartition(".")[-1].upper()
                    image_extension = "JPEG" if image_extension == "JPG" else image_extension
                    image.save(image_io, image_extension, quality=60)
                    new_image = File(image_io, name=image_field.name)
                    setattr(self, field_name, new_image)
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True, default="No Subject")
    message = models.TextField(default="No message provided")

    def __str__(self):
        return self.name


class Information(MainModel):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=UploadToPathAndRename("website"), default='website/default.jpg')
    job = models.CharField(max_length=100, default="Unemployed")
    title = models.CharField(max_length=100, default="Untitled")
    address = models.CharField(max_length=100, default="Not specified")
    city = models.CharField(max_length=30, default="Not specified")
    phone = models.CharField(max_length=15, default="Not specified")
    email = models.EmailField(default="example@example.com")
    git = models.CharField(max_length=100, default="Not specified")
    whatsapp = models.CharField(max_length=100, default="Not specified")
    telegram = models.CharField(max_length=100, default="Not specified")
    instagram = models.CharField(max_length=100, default="Not specified")
    linkedin = models.CharField(max_length=100, null=True, default="Not specified")
    website = models.CharField(max_length=100, default="Not specified")
    birthday = models.DateField(default=date(2000, 1, 1))
    degree = models.CharField(max_length=50, default="Not specified")
    freelance = models.CharField(max_length=50, default="Not specified")
    about_me = models.TextField(default="Not provided")
    about_my_resume = models.TextField(null=True, default="Not provided")
    my_works = models.CharField(max_length=255, null=True, default="No works listed")

    def __str__(self):
        return str(self.author)


class Education(MainModel):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, default="Untitled")
    education = models.CharField(max_length=100, default="Not specified")
    year = models.CharField(max_length=100, default="Not specified")
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.author)


class ProfessionalExperience(MainModel):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, default="Untitled")
    education = models.CharField(max_length=100, default="Not specified")
    year = models.CharField(max_length=100, default="Not specified")
    message = models.TextField(default="No message provided")
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.author)


class Skill(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.TextField(default="Untitled Skill")

    def __str__(self):
        return str(self.author)


class MySkill(models.Model):
    skill_category = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True)
    skill = models.CharField(max_length=20, default="Untitled Skill")
    percent = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.skill_category)


class UserImage(MainModel):
    information = models.ForeignKey(Information, on_delete=models.CASCADE)
    image_more = models.ImageField(upload_to=UploadToPathAndRename("website"), default='website/default.jpg')


class NewsLetter(models.Model):
    email = models.EmailField(default="example@example.com")

    def __str__(self):
        return self.email
