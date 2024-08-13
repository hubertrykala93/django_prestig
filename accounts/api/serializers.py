from rest_framework import serializers
from accounts.models import User, Profile
import re
from datetime import date
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from uuid import uuid4


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
        ]
        extra_kwargs = {
            "date_joined": {
                "format": "%Y-%m-%d %H:%M:%S",
            }
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = [
            "user",
        ]


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
        profilepicture = validated_data.pop("profilepicture", None)

        if profilepicture:
            profilepicture.name = str(uuid4()) + "." + profilepicture.name.split(sep=".")[-1]

            image = Image.open(fp=profilepicture)

            if image.mode == "RGBA":
                image.convert(mode="RGB")

            image = image.resize(size=(300, 300))

            image_io = BytesIO()
            image.save(fp=image_io, format="png")

            instance.profilepicture.delete()
            instance.profilepicture.save(profilepicture.name, ContentFile(image_io.getvalue()), save=False)

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

        if self.context.get("view").__class__.__name__ == "UserLoginAPIView":
            fields = ["username", "repassword", "policy"]

            for field in fields:
                self.fields.pop(field)

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

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                detail=f"The '{username}' already exists.",
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

        return email

    def validate_password(self, password):
        if self.context.get("view").__class__.__name__ == "UserRegisterAPIView":
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
