from django.shortcuts import render
from .models import ProductCategory, Size, Color, Brand, Product, ProductReview, ProductSubCategory
from django.db.models import Count, Prefetch
from blog.views import pagination


def shop(request):
    queryset = Product.objects.filter(is_active=True).order_by("-created_at")

    if request.GET:
        if "sort" in request.GET:
            if request.GET["sort"] == "default":
                queryset = Product.objects.filter(is_active=True).order_by("-created_at")

            if request.GET["sort"] == "alphabetically":
                queryset = Product.objects.filter(is_active=True).order_by("name")

            if request.GET["sort"] == "price":
                queryset = Product.objects.filter(is_active=True).order_by("price")

    return render(
        request=request,
        template_name="shop/shop.html",
        context={
            "title": "Shop",
            "img": "/media/page-title/shop.jpg",
            "queryset": queryset,
            "categories": ProductCategory.objects.filter(is_active=True).annotate(
                product_count=Count('product')
            ).prefetch_related(
                Prefetch('subcategories', queryset=ProductSubCategory.objects.filter(is_active=True))
            ).order_by("-name"),
            "sizes": Size.objects.all(),
            "colors": Color.objects.all().order_by("-name"),
            "brands": Brand.objects.all().order_by("name"),
            "rates": ProductReview.objects.values_list("rate", flat=True).distinct(),
            "pages": pagination(request=request, object_list=queryset, per_page=9),
        }
    )
