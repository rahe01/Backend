from django import forms
from student.models import Profile


GENDER_CHOICES =(
    ('M' , 'Male'),
    ('F' , 'Female'),
    ('O' , 'Other')
)

JOB_CITY_CHOICE = [
    ('Bagerhat', 'Bagerhat'),
    ('Bandarban', 'Bandarban'),
    ('Barguna', 'Barguna'),
    ('Barisal', 'Barisal'),
    ('Bhola', 'Bhola'),
    ('Bogura', 'Bogura'),]



class ProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices = GENDER_CHOICES,
        widget= forms.RadioSelect,
    )
    job_city = forms.MultipleChoiceField(
        choices= JOB_CITY_CHOICE,
        widget= forms.CheckboxSelectMultiple,
        label='Preferred job cities',
        help_text='Select one or more cities'

    )
    class Meta:
        model = Profile
        fields = '__all__'
        labels ={
            'name' : 'Full Name',
            'pin':'Pin Code',
            'mobile': 'Mobile Number'
        }
        help_texts = {
            'profile_image':'Upload  10mb less photo'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'date_of_birth' : forms.DateInput(attrs={'class' : 'form-control' ,'id':'datepicker' , 'type':'date'}),
            'locality': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Write your area name'}),
            'city' : forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Enter your city'}),
            'pin': forms.NumberInput(attrs={'class':'form-control' , 'placeholder':'Enter your Post Code'}),
            'district': forms.Select(attrs={'class':'form-select'}),
            'mobile': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Enter 11 digits number'}),
            'email' : forms.EmailInput(attrs={'class':'form-control' , 'placeholder':'Enter your email'}),
            'profile_image': forms.ClearableFileInput(attrs={
                'onchange': 'previewImage(event)'
            })
            
        }