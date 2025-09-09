from django import forms
from django.core import validators



"""class Registation(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):

        # self.cleaned_data.get['name']
        name_value = self.cleaned_data['name']

        if len(name_value) < 4 :
            raise forms.ValidationError('Enter more than or equal 4 char')
        return name_value
    

    def clean_email(self):

        email_value = self.cleaned_data['email']

        if len(email_value) < 3:

            raise forms.ValidationError("Enter vailid email")
        return email_value"""


"""class Registation(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):

        cleaned_data = super().clean()
        name_value = cleaned_data.get('name')
        email_value = cleaned_data.get('email')
        pass_value = cleaned_data.get('name')
        


        if name_value and len(name_value) < 4:
            self.add_error('name' , 'Enter more than 4')



        return cleaned_data"""

def start_w(value):

    if value[0] != 'r':
        raise forms.ValidationError("R with")



class Registation(forms.Form):
# built in validator
    name = forms.CharField(validators=[validators.MaxLengthValidator(5) , validators.MinLengthValidator(3)] )

    # def custom validator
    email = forms.EmailField(validators=[start_w])
    password = forms.CharField(widget=forms.PasswordInput)

        

        
       