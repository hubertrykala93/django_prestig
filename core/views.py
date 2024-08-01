from django.shortcuts import render
from django.contrib.auth import logout


def index(request):
    print(request.user.is_authenticated)

    return render(
        request=request,
        template_name='core/index.html',
        context={
            "title": "Home",
        })


def about(request):
    logout(request=request)
    return render(
        request=request,
        template_name="core/about.html",
        context={
            "title": "About",
            "img": "/media/page-title/about.jpg",
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
            "img": "/media/page-title/contact.jpg",
        }
    )


def privacy_policy(request):
    return render(
        request=request,
        template_name="core/privacy-policy.html",
        context={
            "title": "Privacy Policy",
        }
    )
