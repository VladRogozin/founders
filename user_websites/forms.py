from django import forms
from .models import UserWebsite

class UserWebsiteForm(forms.ModelForm):
    class Meta:
        model = UserWebsite
        fields = ['html_file', 'css_file', 'js_file']