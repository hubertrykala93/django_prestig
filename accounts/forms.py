from django import forms
from .models import User, Profile, OneTimePassword, DeliveryDetails
from django.contrib.auth.hashers import make_password


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Provide the username", label="User Username")
    email = forms.EmailField(help_text="Provide the e-mail address", label="User E-mail Address")
    password = forms.CharField(help_text="Provide the password", label="User Password", widget=forms.PasswordInput())
    is_verified = forms.BooleanField(help_text="Indicate whether the user is verified.")
    is_active = forms.BooleanField(help_text="Indicate whether the user is active.")
    is_staff = forms.BooleanField(help_text="Indicate whether the user is staff.", required=False)
    is_superuser = forms.BooleanField(help_text="Indicate whether the user is superuser.", required=False)

    class Meta:
        model = User
        fields = "__all__"

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)

        if self.cleaned_data["password"]:
            user.password = make_password(password=self.cleaned_data["password"])

        if commit:
            user.save()

        return user


class OneTimePasswordForm(forms.ModelForm):
    uuid = forms.UUIDField(required=False)

    class Meta:
        model = OneTimePassword
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(OneTimePasswordForm, self).__init__(*args, **kwargs)

        self.fields["user"].help_text = "Select the user for whom a one-time code should be generated."
        self.fields["user"].label = "User"


class ProfileForm(forms.ModelForm):
    firstname = forms.CharField(help_text="Provide the first name.", label="First Name", required=False)
    lastname = forms.CharField(help_text="Provide the last name", label="Last Name", required=False)
    bio = forms.CharField(help_text="Provide a short bio.", label="Bio", required=False)
    gender = forms.ChoiceField(help_text="Select your gender.", label="Gender", choices=(
        ("Male", "Male"),
        ("Female", "Female"),
        ("Undefined", "Undefined"),
    ), widget=forms.RadioSelect, required=False)
    dateofbirth = forms.DateField(help_text="Provide your date of birth", label="Date of Birth", required=False)
    profilepicture = forms.ImageField(help_text="Upload your profile picture.", label="Profile Picture", required=False)
    facebook = forms.CharField(help_text="Provide your Facebook username.", label="Facebook Username", required=False)
    instagram = forms.CharField(help_text="Provide your Instagram username.", label="Instagram Username",
                                required=False)

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


class DeliveryDetailsForm(forms.ModelForm):
    phone = forms.IntegerField(help_text="Provide your phone number.", label="Phone Number")
    country = forms.CharField(help_text="Provide the country.", label="Country")
    state = forms.CharField(help_text="Provide the state.", label="State")
    city = forms.CharField(help_text="Provide the city.", label="City")
    street = forms.CharField(help_text="Provide the street.", label="Street")
    housenumber = forms.CharField(help_text="Provide the house number.", label="House Number")
    apartmentnumber = forms.CharField(help_text="Provide the apartment number.", label="Apartment Number",
                                      required=False)
    postalcode = forms.CharField(help_text="Provide the postal code.", label="Postal Code")

    def __init__(self, *args, **kwargs):
        super(DeliveryDetailsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = DeliveryDetails
        fields = "__all__"
