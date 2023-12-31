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
from django.db.models import Q
from taggit.models import Tag
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1,published_date__lte = timezone.now())
    if kwargs.get('cat_name') != None:
        cat = kwargs.get('cat_name')
        posts = posts.filter(category__name = cat.replace("-", " "))
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__slug__in = [kwargs['tag_name']])
        
    posts = Paginator(posts,2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    tags = Tag.objects.all()
    context = {'posts':posts,'tags':tags} 
    return render (request , 'blog/blog-home.html',context)

def LikePost_View(request):
    post_id = request.GET['post_id']
    post = get_object_or_404(Post, id = post_id)
    like = VoteUser.objects.filter(post= post, user= request.user)
    data = ("item successfully added to cart")
    if like.exists():
        like.delete()
        post.save()
        return JsonResponse({"error": data})
    else:
        VoteUser.objects.create(post= post,  user= request.user)           
        return JsonResponse({"success": data})
        

class Blog_Details_View(View):
    form_class = CommentForm
    template_name = 'blog/blog-details.html'
    
    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post,pk=kwargs['post_id'],slug= kwargs['post_slug'])
        self.images_instance = PostImage.objects.filter(product_id =kwargs['post_id'])
        self.comment_instance = Comment.objects.filter(approach=True,parent=None,post=self.post_instance.id).order_by('created_date')        
        #self.reply_instance = Comment.objects.filter(approach=True,parent__isnull=False,post=self.post_instance.id).order_by('created_date')        
        return super().setup(request, *args, **kwargs)
    def get(self,request,*args, **kwargs):
        form = self.form_class()
        if not self.post_instance.login_require or request.user.is_authenticated:
            print('salaam')
            can_like = False
            if request.user.is_authenticated and self.post_instance.user_can_like(request.user):
                can_like = True
            self.post_instance.counted_views+=1
            self.post_instance.save()
            form = self.form_class()
            content = {'post':self.post_instance,'form':form,'can_like':can_like,'images':self.images_instance,'comments': self.comment_instance}#,"replyes":self.reply_inctance,
            return render (request , self.template_name,content)
        else:
            return redirect("/accounts/login?next="+request.path)
    def post(self,request,*args, **kwargs):
        parent_id = request.POST.get('parent_id')
        form = self.form_class(request.POST)        
        if form.is_valid():
            endcomment = form.save(commit=False)
            endcomment.post = self.post_instance
            if request.user.is_authenticated:
                endcomment.user = request.user
            else:
                endcomment.user = None
            endcomment.parent_id = parent_id
            endcomment.save()
            if parent_id:
                messages.success(request,'Thanks . Your Reply has been received.','success')
            else:
                messages.success(request,'Thanks . Your comment has been received.','success')
        else:
            messages.error(request,'Please inter correct pattern .','error')
        return redirect('blog:blog-details', self.post_instance.id, self.post_instance.slug) 
      


class Searchview(View):
    def get(self,request):
        posts = Post.objects.filter(status=1)
        q = request.GET.get('q')
        posts = posts.filter(content__icontains=q)
        posts = Paginator(posts,2)
        try:
            page_number = request.GET.get('page')
            posts = posts.get_page(page_number)
        except PageNotAnInteger:
            posts = posts.get_page(1)
        except EmptyPage:
            posts = posts.get_page(1)
        context = {'posts':posts}
        return render (request , 'blog/blog-home.html',context)



        
