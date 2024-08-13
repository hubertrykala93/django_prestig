from rest_framework.response import Response
from accounts.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from .serializers import UserRegisterSerializer, UserLoginSerializer, ProfileUpdateSerializer
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import token_generator
from django.shortcuts import redirect
from django.contrib import messages
import os
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login


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

                message = EmailMultiAlternatives(
                    subject="Account activation request.",
                    body=plain_message,
                    from_email=os.environ.get("EMAIL_HOST_USER"),
                    to=[user.email],
                )

                message.attach_alternative(content=html_message, mimetype="text/html")
                message.send()

                return Response(
                    data={
                        "success": f"The account '{serializer.data.get('username')}' has been created. "
                                   f"Check your email to activate it.",
                    },
                    status=status.HTTP_201_CREATED,
                )

            except Exception as e:
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
        messages.info(
            request=request,
            message="Your activation link has expired. Please create your account again."
        )
        return redirect(to="register")

    if user:
        if not user.is_verified:
            if user and token_generator.check_token(user=user, token=token):

                user.is_verified = True
                user.save()

                messages.success(
                    request=request,
                    message="Your account has been activated, you can now log in.",
                )

                return redirect(to="login")

            else:
                user.delete()

                messages.info(
                    request=request,
                    message="Your activation link has expired. Please create your account again."
                )

            return redirect(to="register")

        else:
            messages.info(
                request=request,
                message="Your account is active, you can log in."
            )

            return redirect(to="login")


class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data, context={
            "request": request,
        })

        if User.objects.filter(email=request.data.get("email")).exists():
            user = User.objects.get(email=request.data.get("email"))

            if not user.is_verified:
                return Response(
                    data={
                        "error": "You cannot log in because your account has not been verified yet.",
                    }
                )

        if serializer.is_valid():
            user = authenticate(
                request=request,
                username=User.objects.get(email=serializer.validated_data.get('email')).username,
                password=serializer.validated_data.get("password"),
            )

            if user:
                if "remember" in request.data:
                    request.session.set_expiry(value=365 * 24 * 60 * 60)

                login(request=request, user=user)

                return Response(
                    data={
                        "success": f"Welcome '{serializer.data.get('email')}'. You have successfully logged in.",
                    },
                    status=status.HTTP_200_OK,
                )

            else:
                return Response(
                    data={
                        "error": "Incorrect credentials, please enter the correct information to log in.",
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )


        else:
            return Response(
                data=serializer.errors,
            )


class UserLogoutAPIView(APIView):
    def get(self, request, *args, **kwargs):
        logout(request=request)

        return redirect(to="index")


class UserUpdateAPIView(UpdateAPIView):
    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        return UserRegisterSerializer

    def get_serializer_context(self):
        context = super(UserUpdateAPIView, self).get_serializer_context()

        context["password"] = self.request.data.get("password")

        return context

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data, partial=True)

        if serializer.is_valid():
            self.perform_update(serializer=serializer)

            return Response(
                data={
                    "success": "Your user information has been successfully updated.",
                },
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                data=serializer.errors,
            )

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data, partial=False)

        if serializer.is_valid():
            self.perform_update(serializer=serializer)

            return Response(
                data={
                    "success": "Your user information has been successfully updated.",
                },
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                data=serializer.errors,
            )


class ProfileUpdateAPIView(UpdateAPIView):
    def get_object(self):
        return self.request.user.profile

    def get_serializer_class(self):
        return ProfileUpdateSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data, partial=True)

        if serializer.is_valid():
            self.perform_update(serializer=serializer)

            return Response(
                data={
                    "success": "Your profile information has been successfully updated.",
                },
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                data=serializer.errors,
            )

    def put(self, request, *args, **kwargs):
        instance = self.get_serializer()
        serializer = self.get_serializer(instance=instance, data=request.data, partial=False)

        if serializer.is_valid():
            self.perform_update(serializer=serializer)

            return Response(
                data={
                    "success": "Your profile information has been successfully updated.",
                },
                status=status.HTTP_200_OK
            )

        else:
            return Response(
                data=serializer.errors,
            )
