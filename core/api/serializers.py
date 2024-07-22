from rest_framework import serializers
from core.models import Newsletter
import re
from rest_framework import status


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = "__all__"
        extra_kwargs = {
            "created_at": {
                "format": "%Y-%m-%d %H:%M:%S",
            }
        }


class NewsletterCreateSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    class Meta:
        model = Newsletter
        fields = [
            "id",
            "created_at",
            "email",
        ]
        extra_kwargs = {
            "created_at": {
                "format": "%Y-%m-%d %H:%M:%S",
                "read_only": True,
            },
        }

    def validate_email(self, email):
        if email == "":
            raise serializers.ValidationError(
                detail="E-mail Address is required.",
            )

        if email and not re.match(pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", string=email):
            raise serializers.ValidationError(
                detail="The e-mail address format is invalid.",
            )

        if self.instance is None:
            if email and re.match(pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                                  string=email) and Newsletter.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    detail=f"The newsletter {email} already exists.",
                    code=status.HTTP_400_BAD_REQUEST,
                )
        else:
            if self.instance.email != email and Newsletter.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    detail=f"The newsletter {email} already exists.",
                    code=status.HTTP_400_BAD_REQUEST,
                )

        return email
