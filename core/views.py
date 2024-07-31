from django.shortcuts import render
import requests
from django.http import JsonResponse


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
            return JsonResponse(data=response.json())

        else:
            return JsonResponse(data=response.json())


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
            return JsonResponse(data=response.json())

        else:
            return JsonResponse(data=response.json())


def privacy_policy(request):
    return render(
        request=request,
        template_name="core/privacy-policy.html",
        context={
            "title": "Privacy Policy",
        }
    )
