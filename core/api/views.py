from rest_framework.generics import CreateAPIView
from .serializers import NewsletterCreateSerializer, ContactMailCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
import os


class NewsletterCreateAPIView(CreateAPIView):
    def get_serializer_class(self):
        return NewsletterCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer=serializer)

            try:
                html_message = render_to_string(
                    template_name="core/newsletter-mail.html",
                    context={
                        "email": serializer.validated_data.get("email"),
                    }
                )

                plain_message = strip_tags(html_message)

                message = EmailMultiAlternatives(
                    subject="Thank you for subscribing to our newsletter.",
                    body=plain_message,
                    from_email=os.environ.get("EMAIL_HOST_USER"),
                    to=[serializer.validated_data.get("email")]
                )
                message.attach_alternative(content=html_message, mimetype="text/html")
                message.send(fail_silently=False)

                return Response(
                    data={
                        "success": f"The newsletter '{serializer.data['email']}' has been created successfully.",
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


class ContactMailCreateAPIView(CreateAPIView):
    def get_serializer_class(self):
        return ContactMailCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer=serializer)

            try:
                html_message = render_to_string(
                    template_name="core/contact-mail.html",
                    context={
                        "fullname": serializer.validated_data.get("fullname"),
                        "subject": serializer.validated_data.get("subject"),
                        "email": serializer.validated_data.get("email"),
                        "message": serializer.validated_data.get("message"),
                    }
                )

                plain_message = strip_tags(html_message)

                message = EmailMultiAlternatives(
                    subject="Message from the Prestig website.",
                    body=plain_message,
                    from_email=os.environ.get("EMAIL_HOST_USER"),
                    to=[os.environ.get("EMAIL_HOST_USER")],
                )

                message.attach_alternative(content=html_message, mimetype="text/html")
                message.send()

                return Response(
                    data={
                        "success": "The message has been sent successully.",
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
