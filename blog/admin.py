from django.contrib import admin
from blog.models import Post,Category,Comment,VoteUser,PostImage
# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = PostImage
    fields = ["image"]
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

    def get_fields(self, request, obj=None):
        return ["image", "author", "title", "slug", "content", "category", "counted_views", "status", "published_date",  "login_require"]

    def get_list_display(self, request):
        return ["author", "title", "counted_views", "status"]

    def get_search_fields(self, request):
        return ["author", "title", "counted_views", "status"]

    def get_list_filter(self, request, filters=None):
        return ["author", "title", "counted_views", "status"]
    
class PostComment(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name' ,'post','created_date','approach')
    list_filter = ('post','approach',)
    search_fields = ['name','post']
    
admin.site.register(Category)
admin.site.register(Comment,PostComment)


admin.site.register(VoteUser)


