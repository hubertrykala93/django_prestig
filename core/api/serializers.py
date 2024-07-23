from rest_framework import serializers
from core.models import Newsletter, ContactMail
import re


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
    email = serializers.CharField(allow_blank=True)

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

        if not re.match(pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", string=email):
            raise serializers.ValidationError(
                detail="The e-mail address format is invalid.",
            )

        if Newsletter.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                detail=f"The newsletter {email} already exists.",
            )

        return email


class ContactMailCreateSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(allow_blank=True)
    email = serializers.CharField(allow_blank=True)
    subject = serializers.CharField(allow_blank=True)
    message = serializers.CharField(allow_blank=True)

    class Meta:
        model = ContactMail
        fields = "__all__"
        extra_kwargs = {
            "date_sent": {
                "format": "%Y-%m-%d %H:%M:%S",
                "read_only": True,
            },
        }

    def validate_full_name(self, full_name):
        if full_name == "":
            raise serializers.ValidationError(
                detail="Full name is required.",
            )

        if len(full_name) < 8:
            raise serializers.ValidationError(
                detail="The full name must be at least 8 characters long.",
            )

        return full_name

    def validate_email(self, email):
        if email == "":
            raise serializers.ValidationError(
                detail="E-mail address is required.",
            )

        if not re.match(pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", string=email):
            raise serializers.ValidationError(
                detail="The e-mail address format is invalid.",
            )

        return email

    def validate_subject(self, subject):
        if subject == "":
            raise serializers.ValidationError(
                detail="Subject is required.",
            )

        if len(subject) < 10:
            raise serializers.ValidationError(
                detail="The subject must be at least 8 characters long.",
            )

        return subject

    def validate_message(self, message):
        if message == "":
            raise serializers.ValidationError(
                detail="Message is required.",
            )

        if len(message) < 20:
            raise serializers.ValidationError(
                detail="The message must be at least 20 characters long.",
            )

        return message
