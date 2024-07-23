from rest_framework import serializers
from accounts.models import User
import re
from rest_framework.generics import CreateAPIView


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, allow_blank=True, required=False)
    email = serializers.CharField(max_length=200, allow_blank=True, required=False)
    password = serializers.CharField(max_length=100, allow_blank=True, required=False, write_only=True, style={
        "input_type": "password",
    })

    def __init__(self, *args, **kwargs):
        super(UserRegisterSerializer, self).__init__(*args, **kwargs)

        if not isinstance(self.context.get("view"), CreateAPIView):
            self.fields.pop("username")

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
        ]

    def validate_username(self, username):
        if username == "":
            raise serializers.ValidationError(
                detail="Username is required.",
            )

        if len(username) < 8:
            raise serializers.ValidationError(
                detail="The username must be at least 8 characters long.",
            )

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                detail=f"A user with the username '{username}' already exists.",
            )

        return username

    def validate_email(self, email):
        if email == "":
            raise serializers.ValidationError(
                detail="E-mail Address is required.",
            )

        if not re.match(pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", string=email):
            raise serializers.ValidationError(
                detail="The e-mail address format is invalid.",
            )

        if self.context.get("view").__class__.__name__ == "UserRegisterAPIView":
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    detail=f"A user with this e-mail address '{email}' already exists.",
                )

        if self.context.get("view").__class__.__name__ == "UserLoginAPIView":
            if not User.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    detail=f"The user with the email address '{email}' does not exist.",
                )

        return email

    def validate_password(self, password):
        if password == "":
            raise serializers.ValidationError(
                detail="Password is required.",
            )

        if self.context.get("view").__class__.__name__ == "UserRegisterAPIView":
            if len(password) < 8:
                raise serializers.ValidationError(
                    detail="The password must be at least 8 characters long.",
                )

            if not re.match(pattern="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", string=password):
                raise serializers.ValidationError(
                    detail="The password should contain at least one uppercase letter, one lowercase letter, one number, and one special character.",
                )

        if self.context.get("view").__class__.__name__ == "UserLoginAPIView":
            if User.objects.filter(email=self.context.get("email")).exists():
                if not User.objects.get(email=self.context.get("email")).check_password(raw_password=password):
                    raise serializers.ValidationError(
                        detail=f"Incorrect password for the user '{User.objects.get(email=self.context.get('email')).username}'.",
                    )

        return password

    def create(self, validated_data):
        password = validated_data.pop("password")
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(raw_password=password)

        instance.save()

        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "date_joined",
            "username",
            "email",
            "password",
            "is_verified",
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
        ]
        extra_kwargs = {
            "date_joined": {
                "format": "%Y-%m-%d %H:%M:%S",
            },
            "last_login": {
                "format": "%Y-%m-%d %H:%M:%S",
            },
        }
