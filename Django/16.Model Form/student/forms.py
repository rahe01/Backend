from django import forms
from student.models import Profile


class Registation(forms.ModelForm):
    name = forms.CharField(max_length=55)
    confirm_pass = forms.CharField()

    class Meta:
        model = Profile
        # fields = ['name' , 'email', 'password']
        fields = '__all__'
        exclude = ['name']
        labels = {'name':'Enter name'}
        error_messages = {
            'email':{ 'required':'email field is requred'}
            }
        
        widgets = {
            'password' : forms.PasswordInput(attrs={'class' : 'pwdclass'}),
            'name': forms.TextInput(attrs={'placeholder':'enter name'})
        }