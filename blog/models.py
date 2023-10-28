from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
# Create your models here.
class Post(models.Model): 
    image = models.ImageField(upload_to='blog/%y/%m/%d/',default='blog/defualt.jpg')
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
    image = models.ImageField(upload_to='blog/%y/%m/%d/',default='blog/defualt.jpg')

    def __unicode__(self):
        return self.product.title

    def __str__(self):
        return self.product.title

  