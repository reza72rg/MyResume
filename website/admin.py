from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from website.models import Contact,NewsLetter,Information,Skill,My_Skill,UserImage
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email',)
    list_filter = ('email',)
    search_fields = ('name','message')
    
admin.site.register(Contact,ContactAdmin)
admin.site.register(NewsLetter)
#admin.site.register(Information)



class MySkillkillInline(admin.TabularInline):
    model = My_Skill
    fields = ["skill","percent"]
    extra = 1


@admin.register(Skill)
class SkillAdmin(SummernoteModelAdmin):
    inlines = [MySkillkillInline]

    def get_fields(self, request, obj=None):
        return ["author", "title"]
        
    def get_list_display(self, request):
        return ["author"]

    def get_search_fields(self, request):
        return ["author"]

    def get_list_filter(self, request, filters=None):
        return ["author"]
    def get_summernote_fields (self,request):
        return ['title']




class MyImagekillInline(admin.TabularInline):
    model = UserImage
    fields = ["image_more"]
    extra = 1


@admin.register(Information)
class PostAdmin(SummernoteModelAdmin):
    inlines = [MyImagekillInline]

    def get_fields(self, request, obj=None):
        return ["image","author", "job", "title", 'address',"city", "phone", "email", "whatsapp", "telegram", "instagram", \
            "linkedin","website","birthday","age","degree","freelance","about_me","my_works"]
        
    def get_list_display(self, request):
        return ["author", "email", "age", "phone"]

    def get_search_fields(self, request):
        return ["author", "job"]

    def get_list_filter(self, request, filters=None):
        return ["author", "job"]
    def get_summernote_fields (self,request):
        return ['about_me']


