from django.shortcuts import render
from shop.models import Product, ProductSubCategory, BrandLogo, Brand
from django.db.models import Prefetch


def index(request):
    subcategories = ProductSubCategory.objects.prefetch_related(
        Prefetch("product_set", queryset=Product.objects.filter(is_featured=True).order_by('-created_at'))
    )[:6]

    return render(
        request=request,
        template_name='core/index.html',
        context={
            "title": "Home",
            "new_items": Product.objects.all().order_by("-created_at")[:10],
            "top_selling": Product.objects.all().order_by("-sales_counter")[:10],
            "subcategories": subcategories,
            "brands": Brand.objects.all(),
            "range": range(4),
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


def error404(request, exception=None):
    return render(
        request=request,
        template_name="core/404.html",
        context={
            "title": "Error 404",
        },
        status=404,
    )
