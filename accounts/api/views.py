from rest_framework.response import Response
from accounts.models import User
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework.exceptions import NotFound
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserRegisterAPIView(CreateAPIView):
    def get_view_name(self):
        return "User Register"

    def get_serializer_class(self):
        return UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer=serializer)

            return Response(
                data={
                    "message": f"The user {serializer.data['username']} has been registered successfully.",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
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
