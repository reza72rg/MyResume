from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
    path('blog/',include('blog.urls')),  
    path('captcha/', include('captcha.urls')),
    path('accounts/',include('accounts.urls')),
    path("sitemap.xml",sitemap,{"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap",),
    path('robots.txt', include('robots.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('summernote/', include('django_summernote.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


