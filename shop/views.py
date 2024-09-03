from django.shortcuts import render
from .models import ProductSubCategory, ProductCategory, Size, Color, Brand, Product


def shop(request):
    queryset = Product.objects.filter(is_active=True).order_by("-created_at")

    categories = ProductCategory.objects.prefetch_related("category").all()

    for category in categories:
        print(f"Category -> {category.name}")

        subcategories = category.category.all()

        for subcategory in subcategories:
            print(f"Subcategory -> {subcategory.name}")

    if request.GET:
        if "sort" in request.GET:
            if request.GET["sort"] == "default":
                queryset = Product.objects.filter(is_active=True).order_by("-created_at")

            if request.GET["sort"] == "alphabetically":
                queryset = Product.objects.filter(is_active=True).order_by("-name")

            if request.GET["sort"] == "price":
                queryset = Product.objects.filter(is_active=True).order_by("price")

    return render(
        request=request,
        template_name="shop/shop.html",
        context={
            "title": "Shop",
            "img": "/media/page-title/shop.jpg",
            "queryset": queryset,
            "sizes": Size.objects.all(),
            "colors": Color.objects.all().order_by("-name"),
            "brands": Brand.objects.all().order_by("name"),
        }
    )
