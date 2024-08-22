from rest_framework import serializers
from accounts.models import User, Profile, DeliveryDetails
import re
from datetime import date
from django.contrib.auth import update_session_auth_hash
import os


class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.SerializerMethodField(method_name="get_last_login")

    class Meta:
        model = User
        exclude = [
            "password",
            "groups",
            "user_permissions",
        ]
        extra_kwargs = {
            "date_joined": {
                "format": "%Y-%m-%d %H:%M:%S",
            },
        }

    def get_last_login(self, obj):
        if obj.last_login:
            return obj.last_login.strftime("%Y-%m-%d %H:%M:%S")


class ProfileSerializer(serializers.ModelSerializer):
    profilepicture_name = serializers.SerializerMethodField(method_name="formatted_profile_picture")

    class Meta:
        model = Profile
        fields = "__all__"
        extra_kwargs = {
            "created_at": {
                "format": "%Y-%m-%d %H:%M:%S",
            },
        }

    def formatted_profile_picture(self, obj):
        if obj.profilepicture:
            return obj.profilepicture.name.split("/")[-1]


class ProfileUpdateSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(allow_blank=True)
    lastname = serializers.CharField(allow_blank=True)
    bio = serializers.CharField(allow_blank=True)
    gender = serializers.CharField()
    dateofbirth = serializers.DateField(required=False)
    profilepicture = serializers.ImageField(required=False)
    facebook = serializers.CharField(required=False)
    instagram = serializers.CharField(required=False)

    class Meta:
        model = Profile
        exclude = [
            "user",
        ]

    def validate_firstname(self, firstname):
        if firstname == "":
            raise serializers.ValidationError(
                detail="First Name is required.",
            )

        if len(firstname) < 2:
            raise serializers.ValidationError(
                detail="The first name should consist of at least 2 characters.",
            )

        if len(firstname) > 35:
            raise serializers.ValidationError(
                detail="The first name cannot be longer than 35 characters."
            )

        if not firstname.isalpha():
            raise serializers.ValidationError(
                detail="The first name should contain only letters.",
            )

        return firstname

    def validate_lastname(self, lastname):
        if lastname == "":
            raise serializers.ValidationError(
                detail="Last Name is required.",
            )

        if len(lastname) < 2:
            raise serializers.ValidationError(
                detail="The last name should consist of at least 2 characters."
            )

        if len(lastname) > 35:
            raise serializers.ValidationError(
                detail="The last name cannot be longer than 35 characters.",
            )

        if not lastname.isalpha():
            raise serializers.ValidationError(
                detail="The last name should contain only letters.",
            )

        return lastname

    def validate_bio(self, bio):
        if len(bio) != 0:
            if len(bio) < 10:
                raise serializers.ValidationError(
                    detail="The bio should consist of at least 10 characters.",
                )

            if len(bio) > 150:
                raise serializers.ValidationError(
                    detail="The bio cannot be longer than 150 characters.",
                )

        return bio

    def validate_gender(self, gender):
        gender = gender.capitalize()

        if gender not in ["Undefined", "Female", "Male"]:
            raise serializers.ValidationError(
                detail="Gender must be 'Male' 'Female,' or 'Undefined.'",
            )
        return gender

    def validate_dateofbirth(self, dateofbirth):
        if dateofbirth > date.today():
            raise serializers.ValidationError(
                detail="You cannot enter a future date. Please select a valid date.",
            )

        if not re.match(pattern=r'^\d{4}-\d{2}-\d{2}$', string=dateofbirth.strftime("%Y-%m-%d")):
            raise serializers.ValidationError(
                detail="Invalid date format. The correct format is 'YYYY-MM-DD'.",
            )
        return dateofbirth

    def validate_profilepicture(self, profilepicture):
        allowed_formats = ["jpg", "jpeg", "png", "webp"]

        if profilepicture.name.split(sep=".")[1] not in allowed_formats:
            raise serializers.ValidationError(
                detail="Invalid file format. The correct formats are 'jpeg', 'jpg', 'png', 'webp'.",
            )

        return profilepicture

    def validate_facebook(self, facebook):
        if len(facebook) > 50:
            raise serializers.ValidationError(
                detail="The facebook username cannot be longer than 50 characters.",
            )

        if not re.match(pattern=r'^[a-zA-Z0-9_.-]+$', string=facebook):
            raise serializers.ValidationError(
                detail="The facebook username should contain only letters, digits, dashes, underscores, periods.",
            )
        return facebook

    def validate_instagram(self, instagram):
        if len(instagram) > 50:
            raise serializers.ValidationError(
                detail="The instagram username cannot be longer than 50 characters.",
            )

        if not re.match(pattern=r'^[a-zA-Z0-9_.-]+$', string=instagram):
            raise serializers.ValidationError(
                detail="The instagram username should contain only letters, digits, dashes, underscores, periods.",
            )
        return instagram

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance

    def run_validation(self, data):
        try:
            validated_data = super().run_validation(data=data)

        except serializers.ValidationError as exc:
            new_errors = {field: value[0] if isinstance(value, list) else value for field, value in exc.detail.items()}

            raise serializers.ValidationError(detail=new_errors)

        return validated_data


class ProfilePictureDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["profilepicture"]


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(allow_blank=True)
    email = serializers.CharField(allow_blank=True)
    password = serializers.CharField(allow_blank=True, write_only=True, style={
        "input_type": "password",
    })
    repassword = serializers.CharField(allow_blank=True, write_only=True, style={
        "input_type": "password",
    })
    policy = serializers.BooleanField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "repassword",
            "policy",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.context.get("view").__class__.__name__ == "UserUpdateAPIView":
            self.fields.pop("policy")
            self.fields["password"].allow_blank = False
            self.fields["password"].required = False

            self.fields["repassword"].allow_blank = False
            self.fields["repassword"].required = False

    def validate_username(self, username):
        if username == "":
            raise serializers.ValidationError(
                detail="Username is required.",
            )

        if len(username) < 8:
            raise serializers.ValidationError(
                detail="The username should consist of at least 8 characters.",
            )

        if len(username) > 35:
            raise serializers.ValidationError(
                detail="The username cannot be longer than 35 characters.",
            )

        if self.context.get("view").__class__.__name__ == "UserRegisterAPIView":
            if User.objects.filter(username=username).exists():
                raise serializers.ValidationError(
                    detail=f"The user with the username '{username}' already exists.",
                )
        else:
            if username != self.instance.username:
                if User.objects.filter(username=username).exists():
                    raise serializers.ValidationError(
                        detail=f"The user with the username '{username}' already exists."
                    )

        return username

    def validate_email(self, email):
        if email == "":
            raise serializers.ValidationError(
                detail="E-mail address is required.",
            )

        if len(email) > 255:
            raise serializers.ValidationError(
                detail="The e-mail address cannot be longer than 255 characters.",
            )

        if not re.match(pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", string=email):
            raise serializers.ValidationError(
                detail="The e-mail address format is invalid.",
            )

        if self.context.get("view").__class__.__name__ == "UserRegisterAPIView":
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    detail=f"The user with the e-mail address '{email}' already exists.",
                )

        else:
            if email != self.instance.email:
                if User.objects.filter(email=email).exists():
                    raise serializers.ValidationError(
                        detail=f"The user with the e-mail address '{email}' already exists.",
                    )

        return email

    def validate_password(self, password):
        if password == "":
            raise serializers.ValidationError(
                detail="Password is required",
            )

        if len(password) < 8:
            raise serializers.ValidationError(
                detail="The password should consist of at least 8 characters.",
            )

        if len(password) > 255:
            raise serializers.ValidationError(
                detail="The password cannot be longer than 255 characters.",
            )

        if not re.match(pattern="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", string=password):
            raise serializers.ValidationError(
                detail="The password should contain at least one uppercase letter, one lowercase letter, one number, "
                       "and one special character."
            )

        return password

    def validate_repassword(self, repassword):
        if repassword == "":
            raise serializers.ValidationError(
                detail="Confirm password is required.",
            )

        if len(repassword) > 255:
            raise serializers.ValidationError(
                detail="The confirm password cannot be longer than 255 characters.",
            )

        if repassword != self.context.get("password"):
            raise serializers.ValidationError(
                detail="The confirm password does not match the password.",
            )

        return repassword

    def validate_policy(self, policy):
        if not policy:
            raise serializers.ValidationError(detail="The privacy policy must be accepted.")

        return policy

    def create(self, validated_data):
        validated_data.pop("repassword")
        validated_data.pop("policy")

        password = validated_data.pop("password")

        user = User(**validated_data)

        if password is not None:
            user.set_password(raw_password=password)

        user.save()

        return user

    def update(self, instance, validated_data):
        password = validated_data.get("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password is not None:
            instance.set_password(raw_password=password)

        instance.save()

        update_session_auth_hash(request=self.context.get("request"), user=instance)

        return instance

    def run_validation(self, data):
        try:
            validated_data = super().run_validation(data=data)

        except serializers.ValidationError as exc:
            new_errors = {field: value[0] if isinstance(value, list) else value for field, value in exc.detail.items()}

            raise serializers.ValidationError(detail=new_errors)

        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(allow_blank=True)
    password = serializers.CharField(allow_blank=True, write_only=True, style={
        "input_type": "password",
    })
    remember = serializers.BooleanField(allow_null=True, write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "remember",
        ]

    def validate_email(self, email):
        if email == "":
            raise serializers.ValidationError(
                detail="E-mail is required.",
            )

        if not re.match(pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", string=email):
            raise serializers.ValidationError(
                detail="The e-mail address format is invalid.",
            )

        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                detail=f"No user found with the provided e-mail address. Did you enter it correctly?",
            )

        return email

    def validate_password(self, password):
        from rest_framework import status
        if password == "":
            if self.context.get("request").data.get("email") == "":
                raise serializers.ValidationError(
                    detail="Password is required.",
                )

        if User.objects.filter(email=self.context.get("request").data.get("email")).exists():
            user = User.objects.get(email=self.context.get("request").data.get("email"))

            if user.is_verified:
                if password == "":
                    raise serializers.ValidationError(
                        detail="Password is required.",
                    )
                else:
                    if not user.check_password(raw_password=password):
                        raise serializers.ValidationError(
                            detail=f"You entered an incorrect password for the user '{self.context.get('request').data.get('email')}'."
                        )

        return password

    def run_validation(self, data):
        try:
            validated_data = super().run_validation(data=data)

        except serializers.ValidationError as exc:
            new_errors = {field: value[0] if isinstance(value, list) else value for field, value in exc.detail.items()}

            raise serializers.ValidationError(detail=new_errors)

        return validated_data


class PasswordResetSerializer(serializers.ModelSerializer):
    email = serializers.CharField(allow_blank=True)

    class Meta:
        model = User
        fields = [
            "email",
        ]

    def validate_email(self, email):
        if email == "":
            raise serializers.ValidationError(
                detail="E-mail address is required.",
            )

        if len(email) > 255:
            raise serializers.ValidationError(
                detail="The e-mail address cannot be longer than 255 characters.",
            )

        if not re.match(pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", string=email):
            raise serializers.ValidationError(
                detail="The e-mail address format is invalid.",
            )

        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                detail=f"The user with the provided email address '{email}' does not exist.",
            )

        return email

    def run_validation(self, data):
        try:
            validated_data = super().run_validation(data=data)

        except serializers.ValidationError as exc:
            new_errors = {field: value[0] if isinstance(value, list) else value for field, value in exc.detail.items()}

            raise serializers.ValidationError(detail=new_errors)

        return validated_data


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        allow_blank=True,
        write_only=True,
        style={
            "input_type": "password",
        }
    )
    repassword = serializers.CharField(
        allow_blank=True,
        write_only=True,
        style={
            "input_type": "password",
        }
    )

    class Meta:
        model = User
        fields = [
            "password",
            "repassword",
        ]

    def validate_password(self, password):
        if password == "":
            raise serializers.ValidationError(
                detail="Password is required",
            )

        if len(password) < 8:
            raise serializers.ValidationError(
                detail="The password should consist of at least 8 characters.",
            )

        if len(password) > 255:
            raise serializers.ValidationError(
                detail="The password cannot be longer than 255 characters.",
            )

        if not re.match(pattern="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", string=password):
            raise serializers.ValidationError(
                detail="The password should contain at least one uppercase letter, one lowercase letter, one number, "
                       "and one special character."
            )

        return password

    def validate_repassword(self, repassword):
        if repassword == "":
            raise serializers.ValidationError(
                detail="Confirm password is required.",
            )

        if len(repassword) > 255:
            raise serializers.ValidationError(
                detail="The confirm password cannot be longer than 255 characters.",
            )

        if repassword != self.context.get("password"):
            raise serializers.ValidationError(
                detail="The confirm password does not match the password.",
            )

        return repassword

    def run_validation(self, data):
        try:
            validated_data = super().run_validation(data=data)

        except serializers.ValidationError as exc:
            new_errors = {field: value[0] if isinstance(value, list) else value for field, value in exc.detail.items()}

            raise serializers.ValidationError(detail=new_errors)

        return validated_data


class DeliveryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryDetails
        fields = "__all__"
        extra_kwargs = {
            "created_at": {
                "format": "%Y-%m-%d %H:%M:%S",
            },
        }


class DeliveryDetailsUpdateSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(allow_blank=True)
    country = serializers.CharField(allow_blank=True)
    state = serializers.CharField(allow_blank=True)
    city = serializers.CharField(allow_blank=True)
    street = serializers.CharField(allow_blank=True)
    housenumber = serializers.CharField(allow_blank=True)
    apartmentnumber = serializers.CharField(allow_blank=True, required=False)
    postalcode = serializers.CharField(allow_blank=True)

    class Meta:
        model = DeliveryDetails
        exclude = ["uuid"]

    def validate_phone(self, phone):
        if phone == "":
            raise serializers.ValidationError(
                detail="Phone number is required.",
            )

        if not phone.isdigit():
            raise serializers.ValidationError(
                detail="The phone number should consist of digits only.",
            )

        if len(phone) < 8:
            raise serializers.ValidationError(
                detail="The phone number should contain a minimum of 8 digits.",
            )

        if len(phone) > 20:
            raise serializers.ValidationError(
                detail="The phone number should contain a maximum of 20 digits.",
            )
        return phone

    def validate_country(self, country):
        if country == "":
            raise serializers.ValidationError(
                detail="Country is required.",
            )

        if len(country) < 3:
            raise serializers.ValidationError(
                detail="The country name should contain a minimum of 3 letters.",
            )

        if len(country) > 56:
            raise serializers.ValidationError(
                detail="The country name should contain a maximum of 56 letters.",
            )

        return country

    def validate_state(self, state):
        if state == "":
            raise serializers.ValidationError(
                detail="State is required.",
            )

        if len(state) < 3:
            raise serializers.ValidationError(
                detail="The state name should contain a minimum of 3 letters.",
            )

        if len(state) > 56:
            raise serializers.ValidationError(
                detail="The state name should contain a maximum of 56 letters.",
            )
        return state

    def validate_city(self, city):
        if city == "":
            raise serializers.ValidationError(
                detail="City is required.",
            )

        if len(city) < 3:
            raise serializers.ValidationError(
                detail="The city name should contain a minimum of 3 letters.",
            )

        if len(city) > 169:
            raise serializers.ValidationError(
                detail="The city name should contain a maximum of 169 letters.",
            )
        return city

    def validate_street(self, street):
        if street == "":
            raise serializers.ValidationError(
                detail="Street is required.",
            )

        if len(street) < 3:
            raise serializers.ValidationError(
                detail="The street name should contain a minimum of 3 letters.",
            )

        if len(street) > 50:
            raise serializers.ValidationError(
                detail="The street name should contain a maximum of 50 letters.",
            )
        return street

    def validate_housenumber(self, housenumber):
        if housenumber == "":
            raise serializers.ValidationError(
                detail="House number is required.",
            )

        if not re.match(pattern=r'^[a-zA-Z0-9]+$', string=housenumber):
            raise serializers.ValidationError(
                detail="The house number must consist of letters or digits only.",
            )

        if len(housenumber) > 5:
            raise serializers.ValidationError(
                detail="The house number should contain a maximum of 5 characters.",
            )
        return housenumber

    def validate_apartmentnumber(self, apartmentnumber):
        if not apartmentnumber == "":
            if not re.match(pattern=r'^[a-zA-Z0-9]+$', string=apartmentnumber):
                raise serializers.ValidationError(
                    detail="The apartment number must consist of letters or digits only.",
                )

        if len(apartmentnumber) > 5:
            raise serializers.ValidationError(
                detail="The apartment number should contain a maximum of 5 characters.",
            )

        return apartmentnumber

    def validate_postalcode(self, postalcode):
        if postalcode == "":
            raise serializers.ValidationError(
                detail="Postal Code is required.",
            )

        if len(postalcode) < 5:
            raise serializers.ValidationError(
                detail="The postal code should contain a minimum of 5 characters.",
            )

        if len(postalcode) > 10:
            raise serializers.ValidationError(
                detail="The postal code should contain a maximum of 10 characters.",
            )

        return postalcode

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance

    def run_validation(self, data):
        try:
            validated_data = super().run_validation(data=data)

        except serializers.ValidationError as exc:
            new_errors = {field: value[0] if isinstance(value, list) else value for field, value in exc.detail.items()}

            raise serializers.ValidationError(detail=new_errors)

        return validated_data
