from django import forms
from .models import Newsletter, ContactMail


class NewsletterForm(forms.ModelForm):
    email = forms.CharField(help_text="Provide the e-mail address.", label="E-mail Address")

    class Meta:
        model = Newsletter
        fields = "__all__"


class ContactMailForm(forms.ModelForm):
    fullname = forms.CharField(help_text="Provide the full name.", label="Full Name")
    email = forms.CharField(help_text="Provide the e-mail address.", label="E-mail Address")
    subject = forms.CharField(help_text="Provide the subject of the message.", label="Subject")
    message = forms.CharField(help_text="Provide the message.", label="Message", widget=forms.Textarea)

    class Meta:
        model = ContactMail
        fields = "__all__"
