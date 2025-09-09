from django.contrib import admin

from student.models import Profile






@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display= ('name', 'email')





















# Register your models here.
