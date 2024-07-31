from rest_framework.response import Response
from accounts.models import User
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveDestroyAPIView, GenericAPIView
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework.exceptions import NotFound
import datetime
from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


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
            headers = self.get_success_headers(data=serializer.data)

            return Response(
                data={
                    "success": f"The account '{serializer.data.get('username')}' has been created. "
                               f"Check your email to activate it.",
                    "headers": headers,
                },
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                data=serializer.errors,
            )

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         self.perform_create(serializer=serializer)
    #         headers = self.get_success_headers(data=serializer.data)
    #
    #         return Response(
    #             data={
    #                 "success": f"The account '{serializer.data.get('username')}' has been created. "
    #                            f"Check your email to activate it.",
    #                 "headers": headers,
    #             },
    #             status=status.HTTP_201_CREATED,
    #         )
    #
    #     else:
    #         return Response(
    #             data=serializer.errors,
    #         )

    def get_success_headers(self, data):
        try:
            return {
                "token": Token.objects.get(user=User.objects.get(email=data["email"])).key,
            }
        except (TypeError, KeyError):
            return {}


class UserLoginAPIView(GenericAPIView):
    def get_serializer_class(self):
        return UserRegisterSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()

        context.update(
            {
                "email": self.request.data.get("email")
            },
        )

        return context

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = authenticate(request=request, email=serializer.validated_data.get("email"),
                                password=serializer.validated_data.get("password"))

            if user is not None:
                login(request=request, user=user)
                token, created = Token.objects.get_or_create(user=user)

                return Response(
                    data={
                        "message": "You have been successfully logged in.",
                        "data": {
                            "username": user.username,
                            "email": user.email,
                        },
                        "token": token.key,
                    }
                )

            else:
                return Response(
                    data={
                        "message": "User authentication error, please enter the correct details.",
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            token = Token.objects.get(user=request.user)

        except Token.DoesNotExist:
            return Response(
                data={
                    "message": "Token does not exists.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        token.delete()

        return Response(
            data={
                "message": "You have been successfully logged out.",
            },
            status=status.HTTP_200_OK,
        )


class UsersAPIView(ListAPIView):
    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer

    def get_object(self):
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


class UserDeleteAPIView(RetrieveDestroyAPIView):
    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        id, date_joined, username, email = instance.id, instance.date_joined, instance.username, instance.email

        try:
            self.perform_destroy(instance=instance)

            return Response(
                data={
                    "message": f"The account '{username}' with ID '{id}' has been successfully deleted.",
                    "data": {
                        "id": id,
                        "date_joined": date_joined.strftime("%Y-%m-%d %H:%M:%S"),
                        "username": username,
                        "email": email,
                    },
                    "deleted_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "deleted_by": self.request.user.username,
                },
                status=status.HTTP_200_OK,
            )

        except Exception:
            return Response(
                data={
                    "message": "An error occurred while deleting the object, please try again.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            return Response(
                data={
                    "message": "Account not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        elif isinstance(exc, ValidationError):
            return Response(
                data=exc.detail,
                status=exc.status_code,
            )

        return super().handle_exception(exc)
