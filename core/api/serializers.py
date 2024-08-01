from rest_framework import serializers
from core.models import Newsletter, ContactMail
import re


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

    def run_validation(self, data):
        try:
            validated_data = super().run_validation(data=data)

        except serializers.ValidationError as exc:
            new_errors = {field: value[0] if isinstance(value, list) else value for field, value in exc.detail.items()}

            raise serializers.ValidationError(
                detail=new_errors,
            )

        return validated_data


class ContactMailCreateSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(allow_blank=True)
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

    def validate_fullname(self, fullname):
        if fullname == "":
            raise serializers.ValidationError(
                detail="Full name is required."
            )

        if len(fullname) < 8:
            raise serializers.ValidationError(
                detail="The full name must be at least 8 characters long.",
            )

        return fullname

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

    def run_validation(self, data):
        try:
            validated_data = super().run_validation(data)

        except serializers.ValidationError as exc:
            new_errors = {field: value[0] if isinstance(value, list) else value for field, value in exc.detail.items()}

            raise serializers.ValidationError(
                detail=new_errors
            )

        return validated_data
