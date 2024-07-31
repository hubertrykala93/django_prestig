from rest_framework.response import Response
from accounts.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView
from .serializers import UserRegisterSerializer
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import token_generator
from django.shortcuts import redirect, reverse
from django.contrib import messages
import os
from core.api.exceptions import EmailSendError


class UserRegisterAPIView(CreateAPIView):
    def get_serializer_class(self):
        return UserRegisterSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()

        context["password"] = self.request.data.get("password")

        return context

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer=serializer)
            user = User.objects.get(email=serializer.validated_data.get("email"))

            try:
                html_message = render_to_string(
                    template_name="accounts/account-activation-email.html",
                    context={
                        "user": user,
                        "domain": get_current_site(request=request),
                        "uid": urlsafe_base64_encode(s=force_bytes(s=user.pk)),
                        "token": token_generator.make_token(user=user)
                    }
                )

                plain_message = strip_tags(html_message)

                message = EmailMessage(
                    subject="Account activation request.",
                    body=plain_message,
                    from_email=os.environ.get("EMAIL_HOST_USER"),
                    to=[user.email],
                )

                # message.attach(content=html_message, mimetype="text/html")
                message.content_subtype = "html"
                message.send()

                return Response(
                    data={
                        "success": f"The account '{serializer.data.get('username')}' has been created. "
                                   f"Check your email to activate it.",
                    },
                    status=status.HTTP_201_CREATED,
                )

            except EmailSendError:
                return Response(
                    data={
                        "error": "The message could not be sent.",
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        else:
            return Response(
                data=serializer.errors,
            )


def activate(request, uidb64, token):
    try:
        uid = force_str(s=urlsafe_base64_decode(s=uidb64))
        user = User.objects.get(pk=uid)

    except:
        return redirect(to=reverse(viewname="register"))

    if user and token_generator.check_token(user=user, token=token):
        user.is_verified = True
        user.save()

        messages.success(
            request=request,
            message="Your account has been activated, you can now log in.",
        )

        return redirect(to=reverse(viewname="login"))

    else:
        user.delete()

        messages.info(
            request=request,
            message="Your activation link has expired. Please create your account again."
        )

        return redirect(to=reverse(viewname="register"))
