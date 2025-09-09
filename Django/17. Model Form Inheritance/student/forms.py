from django import forms
from student.models import Profile




class StudentRegistation(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['student_name' , 'email' , 'password']




class TeacherRegistation(StudentRegistation):
    class Meta(StudentRegistation.Meta):
         fields = ['teacher_name' , 'email' , 'password']
