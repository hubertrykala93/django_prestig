from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, \
    RetrieveDestroyAPIView
from core.models import Newsletter
from .serializers import NewsletterSerializer, NewsletterCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from rest_framework.exceptions import ValidationError
from .permissions import NewsletterCustomPermission
from rest_framework.decorators import api_view


@api_view(http_method_names=["GET"])
def api_endpoints(request):
    response = {
        "General": {
            "Method": "GET",
            "URL": "api/v1",
            "Description": "Endpoints",
        },
        "Newsletters": [
            {
                "Method": "GET",
                "URL": "api/v1/newsletters",
                "Description": "Retrieve all newsletters.",
            },
            {
                "Method": "GET",
                "URL": "api/v1/newsletters?ordering=created_at",
                "Description": "Sorts newsletters by created at using the chosen method (ascending, descending) and retrieves them.",
            },
            {
                "Method": "GET",
                "URL": "api/v1/newsletters?ordering=email",
                "Description": "Sorts newsletters by email using the chosen method (ascending, descending) and retrieves them.",
            },
            {
                "Method": "GET",
                "URL": "api/v1/newsletters/<int:pk>",
                "Description": "Retrieve newsletter with a specific ID."
            },
            {
                "Method": "POST",
                "URL": "api/v1/newsletters/create",
                "Description": "Create a new newsletter.",
            },
            {
                "Method": "PATCH/PUT",
                "URL": "api/v1/newsletters/update/<int:pk>",
                "Description": "Update newsletter with a specific ID.",
            },
            {
                "Method": "DELETE",
                "URL": "api/v1/newsletters/delete/<int:pk>",
                "Description": "Deleting newsletter with a specific ID.",
            },
        ],
        "Users": [
            {
                "Method": "GET",
                "URL": "api/v1/users",
                "Description": "Retrieve all users."
            },
            {
                "Method": "GET",
                "URL": "api/v1/users?search={keyword}",
                "Description": "Search and retrieve articles by username or email using a keyword.",
            },
            {
                "Method": "GET",
                "URL": "api/v1/users?ordering=date_joined",
                "Description": "Sorts users by date_joined using the chosen method (ascending, descending) and retrieves them.",
            },
            {
                "Method": "GET",
                "URL": "api/v1/users?ordering=username",
                "Description": "Sorts users by username using the chosen method (ascending, descending) and retrieves them.",
            },
            {
                "Method": "GET",
                "URL": "api/v1/users?ordering=email",
                "Description": "Sorts users by email using the chosen method (ascending, descending) and retrieves them.",
            },
            {
                "Method": "GET",
                "URL": "api/v1/users?ordering=is_verified",
                "Description": "Sorts users by is_verified using the chosen method (ascending, descending) and retrieves them.",
            },
            {
                "Method": "GET",
                "URL": "api/v1/users/<int:pk>",
                "Description": "Retrieve user with a specific ID.",
            },
            {
                "Method": "GET",
                "URL": "api/v1/users/<str:username",
                "Description": "Retrieve user with a specific username.",
            }
        ],
    }
    return Response(
        data=response,
        status=status.HTTP_200_OK,
    )


from rest_framework.permissions import IsAuthenticated


class NewslettersAPIView(ListAPIView):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["created_at", "email"]

    def get_view_name(self):
        return "API Newsletters"

    def get_queryset(self):
        return Newsletter.objects.all()

    def get_serializer_class(self):
        return NewsletterSerializer


class NewsletterRetrieveAPIView(RetrieveAPIView):
    def get_view_name(self):
        return "Newsletter Details"

    def get_queryset(self):
        return Newsletter.objects.all()

    def get_serializer_class(self):
        return NewsletterSerializer


class NewsletterCreateAPIView(CreateAPIView):
    def get_view_name(self):
        return "Newsletter Create"

    def get_serializer_class(self):
        return NewsletterCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer=serializer)

            return Response(
                data={
                    "message": f"The newsletter {serializer.data['email']} has been created successfully.",
                },
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                data={
                    "message": list(serializer.errors.values())[0][0],
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class NewsletterUpdateAPIView(RetrieveUpdateAPIView):
    def get_view_name(self):
        return "Newsletter Update"

    def get_queryset(self):
        return Newsletter.objects.all()

    def get_serializer_class(self):
        return NewsletterCreateSerializer

    def get_permissions(self):
        return [NewsletterCustomPermission()]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        email = instance.email
        serializer = self.get_serializer(data=request.data, instance=instance)

        if serializer.is_valid():
            self.perform_update(serializer=serializer)

            return Response(
                data={
                    "message": f"The newsletter {email} has been successfully updated to {serializer.data.get('email')}.",
                    "data": serializer.data,
                    "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "updated_by": self.request.user.username,
                },
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            return Response(
                data={
                    "message": "Newsletter not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        elif isinstance(exc, ValidationError):
            return Response(
                data=exc.detail,
                status=exc.status_code,
            )

        return super().handle_exception(exc)


class NewsletterDeleteAPIView(RetrieveDestroyAPIView):
    def get_view_name(self):
        return "Newsletter Delete"

    def get_queryset(self):
        return Newsletter.objects.all()

    def get_serializer_class(self):
        return NewsletterSerializer

    def get_permissions(self):
        return [NewsletterCustomPermission()]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        id, created_at, email = instance.id, instance.created_at, instance.email

        try:
            self.perform_destroy(instance=instance)

            return Response(
                data={
                    "message": f"The newsletter {email} has been deleted successfully.",
                    "data": {
                        "id": id,
                        "created_at": created_at.strftime("%Y-%m-%d %H:%M:%S"),
                        "email": email,
                    },
                    "deleted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "deleted_by": self.request.user.username,
                },
                status=status.HTTP_204_NO_CONTENT,
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
                    "message": "Newsletter not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        elif isinstance(exc, ValidationError):
            return Response(
                data=exc.detail,
                status=exc.status_code,
            )

        return super().handle_exception(exc)
