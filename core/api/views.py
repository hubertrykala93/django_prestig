from rest_framework.generics import ListAPIView, CreateAPIView
from core.models import Newsletter
from .serializers import NewsletterSerializer, NewsletterCreateSerializer, ContactMailCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(http_method_names=["GET"])
def api_endpoints(request):
    response = {
        "General": [
            {
                "Method": "GET",
                "URL": "api/v1",
                "Description": "Endpoints",
            },
        ],
        "Newsletters": [
            {
                "Method": "GET",
                "URL": "api/v1/newsletters",
                "Description": "Retrieve all newsletters.",
            },
            {
                "Method": "POST",
                "URL": "api/v1/newsletters/create",
                "Description": "Create a new newsletter.",
            },
        ],
        "Accounts": [
            {
                "Method": "POST",
                "URL": "api/v1/accounts/account-register",
                "Description": "User registration",
            },
            {
                "Method": "POST",
                "URL": "api/v1/accounts/account-login",
                "Description": "User login",
            },
            {
                "Method": "POST",
                "URL": "api/v1/accounts/account-logout",
                "Description": "User logout",
            },
            {
                "Method": "GET",
                "URL": "api/v1/accounts",
                "Description": "Retrieve all accounts."
            },
            {
                "Method": "GET",
                "URL": "api/v1/accounts/<int:pk>",
                "Description": "Retrieve account with a specific ID.",
            },
            {
                "Method": "GET",
                "URL": "api/v1/accounts/<str:username>",
                "Description": "Retrieve account with a specific username.",
            }
        ],
    }
    return Response(
        data=response,
        status=status.HTTP_200_OK,
    )


class NewslettersAPIView(ListAPIView):
    def get_queryset(self):
        return Newsletter.objects.all()

    def get_serializer_class(self):
        return NewsletterSerializer


class NewsletterCreateAPIView(CreateAPIView):
    def get_serializer_class(self):
        return NewsletterCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer=serializer)

            return Response(
                data={
                    "success": f"The newsletter {serializer.data['email']} has been created successfully.",
                },
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class ContactMailCreateAPIView(CreateAPIView):
    def get_serializer_class(self):
        return ContactMailCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer=serializer)

            return Response(
                data={
                    "success": "The message has been sent successfully.",
                },
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
