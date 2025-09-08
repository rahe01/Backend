from django import forms

class Registation(forms.Form):

    f_name = forms.CharField(initial='Rahe' , help_text="Write your name")
    l_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()



GENDER_CHOICES = [('M', 'Male'),('F','Female'),('O', 'Other')]


"""class FormField(forms.Form):

    # Basic fields
    name = forms.CharField()
    email = forms.EmailField()
    pin_code = forms.IntegerField()


    # additional field type
    age = forms.FloatField()
    date_of_birth = forms.DateField()
    appointment_time = forms.TimeField()
    appointment_datetime = forms.DateTimeField()
    is_subscribed = forms.BooleanField()
    agree_terms= forms.NullBooleanField()


    # Choices Field
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    interests = forms.MultipleChoiceField(choices= [('tech','Technology'),('art','Art'),('soprts' , 'Sports')])



    # File and URL Fields
    profile_image = forms.ImageField()
    resume = forms.FileField()
    website = forms.URLField()


    # others specialized fields
    phone_number= forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    password = forms.CharField(widget=forms.PasswordInput())
    slug = forms.SlugField()
    ip_address = forms.GenericIPAddressField()
    rating = forms.DecimalField() """







class FormField(forms.Form):

    # Basic fields
    name = forms.CharField(
        label="Enter Your Name",
        max_length=100,
        label_suffix=": ",
        initial="I am Rahe",
        help_text="Enter your vailid name",
        # validators=
    )
    email = forms.EmailField(
        label="Enter Your Email",
        disabled=True
    )

    pin_code = forms.IntegerField(
        label="Pin Code",
        min_value=100000,
        max_value=999999,
        error_messages={
            'min_value':'Pin code must be at least 6 digits',
            'max_value': 'Pin code can be at most 6 digits'
        }

    )


    # additional field type
    age = forms.FloatField(
        label="Enter Age",
        min_value=0
    )
    date_of_birth = forms.DateField(
        label="Date of Birth",
        required=False,
        help_text="Enter Y-M-D"
    )
    appointment_time = forms.TimeField(
        label="Apppointment time",
        required=False
    )
    appointment_datetime = forms.DateTimeField(
        label="Apppointment time",
        required=False
    )
    is_subscribed = forms.BooleanField(
        label="Apppointment time",
        required=False
    )
    agree_terms= forms.NullBooleanField(
        label="Are you agree"
    )


    # Choices Field
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    interests = forms.MultipleChoiceField(choices= [('tech','Technology'),('art','Art'),('soprts' , 'Sports')])



    # File and URL Fields
    profile_image = forms.ImageField()
    resume = forms.FileField()
    website = forms.URLField()


    # others specialized fields
    phone_number= forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    password = forms.CharField(widget=forms.PasswordInput())
    slug = forms.SlugField()
    ip_address = forms.GenericIPAddressField(
        label="Ip address",
        protocol='both',
        unpack_ipv4= False,
        localize= True
    )
    rating = forms.DecimalField(
        label="Rating",
        max_digits=3,
        decimal_places=1,
        min_value=0,
        max_value=10,
        initial=5.0,
        help_text="Reating provide",
        localize=True
    )