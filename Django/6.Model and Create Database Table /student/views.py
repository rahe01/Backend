from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from student.models import Profile



def home(req):

    return HttpResponse("Hello student")


def student_data(req):

    students = Profile.objects.all()
    

    return render(req, 'student/home.html' , {'students': students} )

def single_student_data(req):

    student = Profile.objects.get(id=2)
    

    return render(req, 'student/single.html' , {'student': student} )

