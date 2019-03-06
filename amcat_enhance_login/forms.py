from amcat_enhance_login.models import amcat_login_with_face_tracker
from django import forms
from django.core import validators


class registration_form(forms.ModelForm):
    class Meta:
        model=amcat_login_with_face_tracker
        fields='__all__'
        
        