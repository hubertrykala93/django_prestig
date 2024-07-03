from django.shortcuts import render


def index(request):
    return render(
        request=request,
        template_name='core/index.html',
        context={
            "title": "Home",
        })


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
