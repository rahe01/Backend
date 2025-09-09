from django.contrib import admin

# Register your models here.

from student.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display =['id' , 'student_name' , 'teacher_name' , 'email']