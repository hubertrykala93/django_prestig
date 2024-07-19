from django import forms
from .models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Provide the username", label="User Username")
    email = forms.EmailField(help_text="Provide the e-mail address", label="User E-mail Address")
    password = forms.CharField(help_text="Provide the password", label="User Password", widget=forms.PasswordInput())
    is_verified = forms.BooleanField(help_text="Indicate whether the user is verified.")
    is_active = forms.BooleanField(help_text="Indicate whether the user is active.")
    is_staff = forms.BooleanField(help_text="Indicate whether the user is staff.")
    is_superuser = forms.BooleanField(help_text="Indicate whether the user is superuser.")

    class Meta:
        model = User
        fields = "__all__"
