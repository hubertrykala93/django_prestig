from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)

        self.fields["email"].help_text = "Provide the e-mail address."

        self.fields["email"].label = "E-mail Address"

    class Meta:
        model = Newsletter
        fields = "__all__"
