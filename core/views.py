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


def create_newsletter(request):
    if request.method == "POST":
        response = requests.post(url="http://127.0.0.1:8000/api/v1/newsletters/create", json={
            "email": request.POST.get("email"),
        })
        
        return JsonResponse(
            data={} if response.status_code == 201 else {
                "email": response.json()["message"]
            }
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
