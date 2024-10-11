from django import template
from blog.models import Post,Category,Comment,VoteUser
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone 

register = template.Library()
@register.simple_tag(name='totalpost')
def total_sum():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='posts')
def total_sum():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snipped(value,arg=10):
    return value[:arg]+' ...'

@register.inclusion_tag('blog/recent-posts.html')
def recent_posts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:4]
    return { 'posts':posts }

@register.inclusion_tag('blog/populare-posts.html')
def populare_posts():
    posts = Post.objects.filter(status=1).order_by('-counted_views')[:2]
    return { 'posts':posts }

@register.inclusion_tag('blog/categories_posts.html')
def categories_posts():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    nule_new=dict(sorted(cat_dict.items(),key=lambda x:x[1],reverse=True))
    return {'cat_dict':nule_new}


@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid,approach=True).count()

@register.simple_tag(name='likes_count')
def function_like(pid):
    return VoteUser.objects.filter(post=pid).count()


@register.inclusion_tag('blog/blog-nextpage.html')
def nextpage(pid):
    posts = Post.objects.filter(status=1,published_date__lte = timezone.now())
    mylist = []
    for i in posts:
        mylist.append(i.id)
    len_posts = len(posts)
    Prev_post = mylist.index(pid)
    Next_post = mylist.index(pid)+2
    if Prev_post != 0:
        Prev_post = posts.get(id=Prev_post)
    if Next_post <= len_posts:
        Next_post = posts.get(id=Next_post)
    else:
        pass
    return {'Prev_post':Prev_post,'Next_post':Next_post}
        