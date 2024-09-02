from django.shortcuts import render
from .models import ProductSubCategory, ProductCategory, Size, Color, Brand


def shop(request):
    categories = ProductCategory.objects.all()
    for category in categories:
        print(category.name)
        print(category.category.all())

    return render(
        request=request,
        template_name="shop/shop.html",
        context={
            "title": "Shop",
            "img": "/media/page-title/shop.jpg",
            "sizes": Size.objects.all(),
            "colors": Color.objects.all().order_by("-name"),
            "brands": Brand.objects.all().order_by("name"),
        }
    )
