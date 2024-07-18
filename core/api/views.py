from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, \
    RetrieveDestroyAPIView
from core.models import Newsletter
from .serializers import NewsletterSerializer, NewsletterCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import CustomNewsletterPermission


class NewsletterAPIView(ListAPIView):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["created_at", "email"]

    def get_view_name(self):
        return "API Newsletters"

    def get_queryset(self):
        return Newsletter.objects.all()

    def get_serializer_class(self):
        return NewsletterSerializer

    def get_permissions(self):
        return [CustomNewsletterPermission()]


class NewsletterRetrieveAPIView(RetrieveAPIView):
    def get_queryset(self):
        return Newsletter.objects.all()

    def get_serializer_class(self):
        return NewsletterSerializer

    def get_permissions(self):
        return [CustomNewsletterPermission()]


class NewsletterCreateAPIView(CreateAPIView):
    def get_serializer_class(self):
        return NewsletterCreateSerializer

    def get_permissions(self):
        return [CustomNewsletterPermission()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer=serializer)

            return Response(
                data={
                    "message": f"The newsletter {serializer.data['email']} has been created successfully.",
                    "data": serializer.data,
                    "created_by": self.request.user.username,
                },
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class NewsletterUpdateAPIView(RetrieveUpdateAPIView):
    def get_queryset(self):
        return Newsletter.objects.all()

    def get_serializer_class(self):
        return NewsletterCreateSerializer

    def get_permissions(self):
        return [CustomNewsletterPermission()]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=instance)

        if serializer.is_valid():
            self.perform_update(serializer=serializer)

            return Response(
                data={
                    "message": "The newsletter has been updated successfully.",
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


class NewsletterDeleteAPIView(RetrieveDestroyAPIView):
    def get_queryset(self):
        return Newsletter.objects.all()

    def get_serializer_class(self):
        return NewsletterSerializer

    # def get_permissions(self):
    #     return [CustomNewsletterPermission()]

    def delete(self, request, *args, **kwargs):
        print(self.headers)
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
                    "An error occurred while deleting the object, please try again."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
