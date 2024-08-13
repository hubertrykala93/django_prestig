from django import forms
from .models import User, Profile


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


class ProfileForm(forms.ModelForm):
    firstname = forms.CharField(help_text="Provide the first name.", label="First Name", required=False)
    lastname = forms.CharField(help_text="Provide the last name", label="Last Name", required=False)
    bio = forms.CharField(help_text="Provide a short bio.", label="Bio", required=False)
    gender = forms.ChoiceField(help_text="Select your gender.", label="Gender", choices=(
        ("Male", "Male"),
        ("Female", "Female"),
        ("Undefined", "Undefined"),
    ), widget=forms.RadioSelect, required=False)
    dateofbirth = forms.DateTimeField(help_text="Provide your date of birth", label="Date of Birth", required=False)
    profilepicture = forms.ImageField(help_text="Upload your profile picture.", label="Profile Picture", required=False)
    facebook = forms.CharField(help_text="Provide your Facebook username.", label="Facebook Username", required=False)
    instagram = forms.CharField(help_text="Provide your Instagram username.", label="Instagram Username", required=False)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields["user"].help_text = "Select a user."
        self.fields["user"].label = "User"

        self.fields["wishlist"].help_text = "Add products to favourites."
        self.fields["wishlist"].label = "Wishlist"
        self.fields["wishlist"].required = False

        self.fields["delivery_details"].help_text = "Choose delivery options."
        self.fields["delivery_details"].label = "Delivery Details"
        self.fields["delivery_details"].required = False

    class Meta:
        model = Profile
        fields = "__all__"
