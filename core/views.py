from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
import os
from .exceptions import EmailSendError


def index(request):
    return render(
        request=request,
        template_name='core/index.html',
        context={
            "title": "Home",
        })


def about(request):
    return render(
        request=request,
        template_name="core/about.html",
        context={
            "title": "About",
            "img": "/media/page-title/about.jpg",
        }
    )


def create_newsletter(request):
    if request.method == "POST":
        email = request.POST.get("email").strip()
        response = requests.post(url="http://127.0.0.1:8000/api/v1/newsletters/create", json={
            "email": email,
        })

        if response.status_code == 201:
            try:
                html_message = render_to_string(
                    template_name="core/newsletter-mail.html",
                    context={
                        "email": email,
                    }
                )
                plain_message = strip_tags(html_message)

                message = EmailMultiAlternatives(
                    subject="Thank you for subscribing to our newsletter.",
                    body=plain_message,
                    from_email=os.environ.get("EMAIL_FROM"),
                    to=[email],
                )
                message.attach_alternative(content=html_message, mimetype="text/html")
                message.send(fail_silently=False)

                return JsonResponse(data=response.json(), status=response.status_code)

            except EmailSendError:
                return JsonResponse(
                    data=response.json(),
                    status=500,
                )

        else:
            return JsonResponse(
                data=response.json(),
            )


def shop(request):
    return render(
        request=request,
        template_name="core/shop.html",
        context={
            "title": "Shop",
        }
    )


def product(request):
    return render(
        request=request,
        template_name="core/product.html",
        context={
            "title": "Product",
        }
    )


def blog(request):
    return render(
        request=request,
        template_name="core/blog.html",
        context={
            "title": "Blog",
        }
    )


def contact_us(request):
    return render(
        request=request,
        template_name="core/contact-us.html",
        context={
            "title": "Contact Us",
            "img": "/media/page-title/contact.jpg",
        }
    )


def send_contact_mail(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        response = requests.post(
            url='http://127.0.0.1:8000/api/v1/contact-mails/create',
            json={
                "fullname": fullname,
                "email": email,
                "subject": subject,
                "message": message,
            }
        )

        if response.status_code == 201:
            try:
                html_message = render_to_string(
                    template_name="core/contact-mail.html",
                    context={
                        "fullname": fullname,
                        "subject": subject,
                        "email": email,
                        "message": message,
                    },
                )

                plain_message = strip_tags(html_message)

                message = EmailMultiAlternatives(
                    subject="Message from the Prestig website.",
                    body=plain_message,
                    from_email=os.environ.get("EMAIL_HOST_USER"),
                    to=[os.environ.get("EMAIL_HOST_USER")]
                )
                message.attach_alternative(content=html_message, mimetype="text/html")
                message.send()

                return JsonResponse(
                    data=response.json(),
                    status=response.status_code,
                )

            except EmailSendError:
                return JsonResponse(
                    data={
                        "error": "Error sending the message, please try again.",
                    },
                    status=500,
                )

        else:
            return JsonResponse(data=response.json(), status=response.status_code)


def privacy_policy(request):
    return render(
        request=request,
        template_name="core/privacy-policy.html",
        context={
            "title": "Privacy Policy",
        }
    )
