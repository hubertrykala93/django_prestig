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


def create_newsletter(request):
    if request.method == "POST":
        email = request.POST.get("email").strip()
        response = requests.post(url="http://127.0.0.1:8000/api/v1/newsletters/create", json={
            "email": email,
        })

        if response.status_code == 201:
            try:
                html_message = render_to_string(
                    template_name="core/newsletter_mail.html",
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

                return JsonResponse(data={}, status=response.status_code)

            except EmailSendError:
                return JsonResponse(
                    data={},
                    status=500,
                    safe=False,
                )

        else:
            return JsonResponse(
                data={
                    "email": response.json()["message"],
                },
                status=response.status_code,
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
        }
    )


def send_contact_mail(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname").strip()
        email = request.POST.get("email").strip()
        subject = request.POST.get("subject").strip()
        message = request.POST.get("message").strip()

        response = requests.post(
            url='http://127.0.0.1:8000/api/v1/contact-mails/create',
            json={
                "fullname": fullname,
                "email": email,
                "subject": subject,
                "message": message,
            }
        )
        print(response.json())
        print(response.status_code)

        if response.status_code:
            return JsonResponse(
                data={}, status=201
            )

        else:
            return JsonResponse(data=response.json(), status=400)
