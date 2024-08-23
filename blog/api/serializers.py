from blog.models import ArticleComment
from rest_framework import serializers
import re
from accounts.models import User


class CommentSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(allow_blank=True, required=False)
    email = serializers.CharField(allow_blank=True, required=False)
    comment = serializers.CharField(allow_blank=True)

    class Meta:
        model = ArticleComment
        fields = [
            "fullname",
            "email",
            "comment",
        ]

    def validate_fullname(self, fullname):
        if fullname == "":
            raise serializers.ValidationError(
                detail="Fullname is required.",
            )

        if not fullname.replace(" ", "").isalpha():
            raise serializers.ValidationError(
                detail="The fullname should contain only letters.",
            )

        if len(fullname) < 2:
            raise serializers.ValidationError(
                detail="The fullname should consist of at least 2 characters long.",
            )

        if len(fullname) > 35:
            raise serializers.ValidationError(
                detail="The fullname cannot be longer than 35 characters.",
            )

        return fullname

    def validate_email(self, email):
        if email == "":
            raise serializers.ValidationError(
                detail="E-mail address is required.",
            )

        if len(email) > 255:
            raise serializers.ValidationError(
                detail="The email cannot be longer than 255 characters.",
            )

        if not re.match(pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", string=email):
            raise serializers.ValidationError(
                detail="The e-mail address format is invalid.",
            )

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                detail="You cannot use this e-mail address.",
            )

        return email

    def validate_comment(self, comment):
        if comment == "":
            raise serializers.ValidationError(
                detail="Comment is required.",
            )

        if len(comment) < 5:
            raise serializers.ValidationError(
                detail="The comment should consist of at least 5 characters long.",
            )

        if len(comment) > 200:
            raise serializers.ValidationError(
                detail="The comment cannot be longer than 200 characters.",
            )

        return comment

    def create(self, validated_data):
        comment = ArticleComment(**validated_data)
        comment.save()

        return validated_data

    def run_validation(self, data):
        try:
            validated_data = super().run_validation(data=data)

        except serializers.ValidationError as exc:
            new_errors = {field: value[0] if isinstance(value, list) else value for field, value in exc.detail.items()}

            raise serializers.ValidationError(detail=new_errors)

        return validated_data
