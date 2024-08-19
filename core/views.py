from django.shortcuts import render


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


def product(request):
    return render(
        request=request,
        template_name="core/product.html",
        context={
            "title": "Product",
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


def error404(request, exception):
    return render(
        request=request,
        template_name="core/404.html",
        context={
            "title": "Error 404",
        },
        status=404,
    )