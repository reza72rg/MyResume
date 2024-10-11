from django.urls import path
from blog.views import * 
from django.contrib.sitemaps.views import sitemap
from blog.feeds import LatestEntriesFeed
app_name = 'blog'

urlpatterns = [
    path('',blog_view, name ='blog'),
    path('post-<int:post_id>/<slug:post_slug>/',Blog_Details_View.as_view(), name ='blog-details'),
    path('category/<str:cat_name>/',blog_view, name ='category'),
    path('tag/<str:tag_name>/',blog_view, name ='tag'),
    path('author/<str:author_username>/',blog_view,name ='author'),
    path('search/',Searchview.as_view(),name ='search'),
    path('rss/feed/', LatestEntriesFeed()),
    path('like/',LikePost_View, name ='like'),
    ]
 