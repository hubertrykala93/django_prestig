from rest_framework.response import Response
from accounts.models import User
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework.exceptions import NotFound
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.template.loader import render_to_string
from random import randint
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site
from django.utils.html import strip_tags
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from .tokens import token_generator
import uuid
import os


class UserRegisterAPIView(CreateAPIView):
    def get_view_name(self):
        return "User Register"

    def get_serializer_class(self):
        return UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer=serializer)

            user = User.objects.get(username=serializer.data.get("username"))

            print('before try')
            try:
                print('start try')
                print('html_message')
                print(user)
                print(get_current_site(request=request))
                print(urlsafe_base64_encode(s=force_bytes(s=user.pk)))
                html_message = render_to_string(
                    template_name="accounts/activation_email.html",
                    context={
                        "user": user,
                        "domain": get_current_site(request=request),
                        "uid": urlsafe_base64_encode(s=force_bytes(s=user.pk)),
                        # "token": token_generator.make_token(user=user),
                    },
                )

                print('plain_message')
                plain_message = strip_tags(html_message)

                print('message')
                message = EmailMultiAlternatives(
                    subject="Account activation request.",
                    body=plain_message,
                    from_email=os.environ.get("EMAIL_HOST_USER"),
                    to=[user.email],
                )

                print('messsage attach_alternative')
                message.attach_alternative(
                    content=html_message, mimetype="text/html"
                )
                print(user.email)
                print('presend')
                message.send(fail_silently=True)
                print('send')

                return Response(
                    data={
                        "message": f"The user {serializer.data['username']} has been registered successfully.",
                        "data": serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )

            except Exception as e:
                print('start except')
                return Response(
                    data="Błąd wysyłania maila."
                )

        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class UsersAPIView(ListAPIView):
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ["username", "email"]
    ordering_fields = ["date_joined", "username", "email", "is_verified"]

    def get_view_name(self):
        return "API Users"

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    def get_view_name(self):
        return "User Details"

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer

    def get_object(self):
        print(self.kwargs.get("pk"))
        if self.kwargs.get("pk"):
            if self.get_queryset().filter(id=self.kwargs.get("pk")).exists():
                obj = self.get_queryset().filter(id=self.kwargs.get("pk")).first()

            else:
                raise NotFound(
                    detail={
                        "message": f"The user with ID '{self.kwargs.get('pk')}' does not exist.",
                    }
                )

        elif self.kwargs.get("username"):
            if self.get_queryset().filter(username=self.kwargs.get("username")).exists():
                obj = self.get_queryset().filter(username=self.kwargs.get("username")).first()

            else:
                raise NotFound(
                    detail={
                        "message": f"The user with the username '{self.kwargs.get('username')}' does not exist.",
                    },
                )

        else:
            return Response(
                data={
                    "message": "The user does not exist."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        return obj
