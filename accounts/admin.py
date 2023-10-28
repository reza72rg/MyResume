from django.contrib import admin
from accounts.models import ProfileUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = ProfileUser
    can_delete = False
class ExtendProfile(UserAdmin):
    inlines = (ProfileInline,)
admin.site.unregister(User)
admin.site.register(User, ExtendProfile)
