from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'student/home.html')

def course(request):
    return render(request, 'student/course.html')

def result(request):
    return render(request, 'student/result.html')