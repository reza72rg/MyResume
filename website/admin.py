from django.contrib import admin

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
class SkillAdmin(admin.ModelAdmin):
    inlines = [MySkillkillInline]


class MyImagekillInline(admin.TabularInline):
    model = UserImage
    fields = ["image_more"]
    extra = 1


@admin.register(Information)
class ImageAdmin(admin.ModelAdmin):
    inlines = [MyImagekillInline]
