from rest_framework import serializers
from accounts.models import User
import re


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

    def validate_username(self, username):
        if username == "":
            raise serializers.ValidationError(
                detail="Username is required.",
            )

        if len(username) < 8:
            raise serializers.ValidationError(
                detail="The username should consist of at least 8 characters.",
            )

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                detail=f"The {username} already exists.",
            )

        return username

    def validate_email(self, email):
        if email == "":
            raise serializers.ValidationError(
                detail="E-mail address is required.",
            )

        if not re.match(pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", string=email):
            raise serializers.ValidationError(
                detail="The e-mail address format is invalid.",
            )

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                detail=f"The user with the e-mail address {email} already exists.",
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
