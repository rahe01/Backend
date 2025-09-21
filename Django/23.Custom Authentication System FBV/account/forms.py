from django import forms
from account.models import User


class RegistationForm (forms.ModelForm):
    ROLE_CHOICES = (
        ('seller' , 'Seller'),
        ('customer' , 'Customer')
    )
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=ROLE_CHOICES , widget=forms.Select)

    class Meta:
        model = User
        fields =["email", "name" , "password" , "confirm_password"]

        def clean(self):
            cleaned_data = super().celan()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password != confirm_password:
                self.add_error("confirm_password" , "Password does not match")

            return cleaned_data
        
        def clean_email(self):
            email = self.cleaned_data.get("email")
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email already exists")
            return email
            

class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        max_length=255,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder':'enter mail'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not User.objects.filter(email = email).exists():
            raise forms.ValidationError(('No account'))
        
        return email