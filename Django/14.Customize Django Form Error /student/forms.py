from django import forms



class Registation(forms.Form):

    name = forms.CharField( error_messages={'required': 'Name is required'} , max_length=2 )
    email = forms.EmailField( error_messages={'required': 'Email is required'}, max_length=10)
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required': 'Pass is required'})