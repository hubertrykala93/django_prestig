from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "date_joined",
            "username",
            "email",
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
