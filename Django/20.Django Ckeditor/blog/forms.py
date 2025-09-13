from django import forms
from blog.models import BlogPost
from django_ckeditor_5.widgets import CKEditor5Widget


class CreatePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
              "content": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
          }
