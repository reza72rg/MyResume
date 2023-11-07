from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _
from django.db.models.fields.files import ImageFieldFile
from PIL import Image
from io import BytesIO
from django.core.files import File


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


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
# Create your models here.

class Post(MainModel): 
    image = models.ImageField(upload_to='blog',default='blog/defualt.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, related_name='posts_author')
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    #tags = TaggableManager()

    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    login_require = models.BooleanField(default=False)
    
    def get_absolute_url(self):
       return reverse("blog:blog-details", args=(self.id, self.slug))
    def __str__(self):
        return self.title
    
    def like_count(self):
       return self.upost.count()
   
    def user_can_like(self, user):
        user_like = user.uvote.filter(post = self)
        if user_like.exists():
            return True
        return False
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    approach = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.name
    
class VoteUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uvote')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='upost')
    
    def __str__(self):
        return f'{self.user} --> like this post-->  {self.post.slug}' 
    
class PostImage(models.Model):
    product = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog',default='blog/defualt.jpg')

    def __unicode__(self):
        return self.product.title

    def __str__(self):
        return self.product.title

  