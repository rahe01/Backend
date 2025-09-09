from django.contrib import admin
from student.models import UserProfile

# Register your models here.

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'email' , 'password')
