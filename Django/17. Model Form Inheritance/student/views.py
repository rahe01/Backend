from django.shortcuts import render
from django.http import HttpResponse
from student.forms import StudentRegistation , TeacherRegistation
from django.http import HttpResponseRedirect


# Create your views here.


def home(req):

    return HttpResponse("Home page")



def student_form_view(req):

    if req.method == 'POST':
        form = StudentRegistation(req.POST)
        if form.is_valid():
            form.save()


    else:
        form = StudentRegistation()

    return render(req, 'student/student.html', {'form':form})

def teacher_form_view(req):

    if req.method == 'POST':
        form = TeacherRegistation(req.POST)
        if form.is_valid():
            form.save()
    else:
        form = TeacherRegistation()

    return render(req, 'student/teacher.html', {'form':form})

