from django.shortcuts import render, redirect
from .models import Product, ProductTags, ProductCategory, ProductSubCategory, Color, Brand
from blog.views import pagination
from django.contrib import messages
from django.db.models import Avg


def sort_products(request, queryset):
    if request.GET:
        if "sort" in request.GET:
            if request.GET["sort"] == "default":
                return queryset.order_by("-created_at")

            elif request.GET["sort"] == "alphabetically":
                return queryset.order_by("name")

            elif request.GET["sort"] == "price":
                return queryset.order_by("price")

            else:
                return queryset.order_by("-created_at")

        else:
            return queryset.order_by("-created_at")

    else:
        return queryset.order_by("-created_at")


def shop(request):
    queryset = Product.objects.filter(is_active=True)
    queryset = sort_products(request=request, queryset=queryset)

    if "category" in request.GET:
        selected_categories = ProductCategory.objects.filter(name__in=request.GET.getlist("category"))

        queryset = queryset.filter(category__in=selected_categories)

    if "subcategory" in request.GET:
        queryset = queryset.filter(subcategory__name__in=request.GET.getlist("subcategory"))

    if "color" in request.GET:
        queryset = queryset.filter(stock__color__id=Color.objects.get(name=request.GET["color"]).id)

    if "size" in request.GET:
        queryset = queryset.filter(stock__size__name__in=request.GET.getlist("size"))

    if "brand" in request.GET:
        brands = Brand.objects.filter(name__in=request.GET.getlist("brand"))

        queryset = queryset.filter(brand__in=brands)

    queryset = queryset.annotate(avg_rating=Avg("productreview__rate"))

    if "rating" in request.GET:
        selected_ratings = list(map(int, request.GET.getlist("rating")))

        if selected_ratings:
            min_rating = min(selected_ratings)
            queryset = queryset.filter(avg_rating__gte=min_rating)

    return render(
        request=request,
        template_name="shop/shop.html",
        context={
            "title": "Shop",
            "img": "/media/page-title/shop.jpg",
            "pages": pagination(request=request, object_list=queryset, per_page=9),
            "checked_categories": request.GET.getlist("category"),
            "checked_subcategories": request.GET.getlist("subcategory"),
            "checked_sizes": request.GET.getlist("size"),
            "checked_brands": request.GET.getlist("brand"),
            "checked_ratings": request.GET.getlist("rating"),
        }
    )


def products_by_tag(request, tag_slug):
    try:
        tag = ProductTags.objects.get(slug=tag_slug)

    except ProductTags.DoesNotExist:
        messages.info(
            request=request,
            message=f"The tag named '{tag_slug.replace('-', ' ').title()}' does not exist."
        )

        return redirect(to="shop")

    queryset = Product.objects.filter(tags=tag, is_active=True)
    queryset = sort_products(request=request, queryset=queryset)

    return render(
        request=request,
        template_name="shop/shop.html",
        context={
            "title": "Shop",
            "tag": tag.name,
            "img": "/media/page-title/shop.jpg",
            "pages": pagination(request=request,
                                object_list=queryset,
                                per_page=9)
        }
    )


def products_by_category(request, category_slug):
    try:
        category = ProductCategory.objects.get(slug=category_slug)

    except ProductCategory.DoesNotExist:
        messages.info(
            request=request,
            message=f"The category named '{category_slug.replace('-', ' ').title()}' does not exist."
        )

        return redirect(to="shop")

    queryset = Product.objects.filter(category=category, is_active=True)
    queryset = sort_products(request=request, queryset=queryset)

    return render(
        request=request,
        template_name="shop/shop.html",
        context={
            "title": "Shop",
            "category": category.name,
            "img": "/media/page-title/shop.jpg",
            "pages": pagination(request=request,
                                object_list=queryset,
                                per_page=9)
        }
    )


def products_by_subcategory(request, subcategory_slug):
    if not ProductSubCategory.objects.filter(slug=subcategory_slug).exists():
        messages.info(
            request=request,
            message=f"The subcategory named '{subcategory_slug.replace('-', ' ').title()}' does not exist."
        )

        return redirect(to="shop")

    subcategories = ProductSubCategory.objects.filter(slug=subcategory_slug)

    queryset = Product.objects.filter(subcategory__in=subcategories, is_active=True)
    queryset = sort_products(request=request, queryset=queryset)

    return render(
        request=request,
        template_name="shop/shop.html",
        context={
            "title": "Shop",
            "subcategory": subcategory_slug.replace('-', ' ').title(),
            "img": "/media/page-title/shop.jpg",
            "pages": pagination(request=request,
                                object_list=queryset,
                                per_page=9),
        }
    )


def product_details(request, category_slug, subcategory_slug, product_slug):
    category = ProductCategory.objects.get(slug=category_slug)
    subcategory = ProductSubCategory.objects.get(category=category, slug=subcategory_slug)
    product = Product.objects.get(category=category, subcategory=subcategory, slug=product_slug)

    return render(
        request=request,
        template_name="shop/product-details.html",
        context={
            "title": product.name,
            "category": category,
            "subcategory": subcategory,
            "product": product,
        }
    )
