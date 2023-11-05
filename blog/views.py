from typing import Any
from django import http
from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post,PostImage
from django.utils import timezone
from blog.forms import  CommentForm
from blog.models import Post,Comment,VoteUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1,published_date__lte = timezone.now())
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
        
    context = {'posts':posts} 
    return render (request , 'blog/blog-home.html',context)


class Blog_Details_View(LoginRequiredMixin, View):
    form_class = CommentForm
    template_name = 'blog/blog-details.html'
    
    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post,pk=kwargs['post_id'],slug= kwargs['post_slug'])
        self.images_instance = PostImage.objects.filter(product_id =kwargs['post_id'])
        self.comment_inctance = Comment.objects.filter(approach=True,post=self.post_instance.id).order_by('created_date')
        return super().setup(request, *args, **kwargs)
    
    def get(self,request,*args, **kwargs):
        if not self.post_instance.login_require:
         
            can_like = False
            if request.user.is_authenticated and self.post_instance.user_can_like(request.user):
                can_like = True
            self.post_instance.counted_views +=1
            self.post_instance.save()
            form = self.form_class()
            content = {'post':self.post_instance,'comment': self.comment_inctance,'form':form,'can_like':can_like,'images':self.images_instance}
            return render (request , self.template_name,content)
        else:
            return redirect('accounts:login')
    def post(self,request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            newcomment = form.save(commit=False)
            newcomment.post = self.post_instance
            newcomment.save()
            messages.success(request,'Thanks . Thanks . Your message has been received.','success')
        return redirect('blog:blog-details', self.post_instance.id, self.post_instance.slug) 
      


class Searchview(View):
    def get(self,request):
        posts = Post.objects.filter(status=1)
        posts = posts.filter(content__contains=request.GET.get('s'))
        context = {'posts':posts}
        return render (request , 'blog/blog-home.html',context)



class LikePost_View(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id = post_id)
        like = VoteUser.objects.filter(post= post, user= request.user)
        if like.exists():
            messages.error(request, 'You already liked this post','danger')
        else:
            VoteUser.objects.create(post= post,  user= request.user)           
            messages.success(request, 'you liked this post','success')
        return redirect('blog:blog-details' , post.id, post.slug)
        
class UnLikePost_View(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id = post_id)
        like = VoteUser.objects.filter(post= post, user= request.user)
        if like.exists():
            like.delete()
            messages.success(request, 'You unlike  this post','success')
        return redirect('blog:blog-details' , post.id, post.slug)
        