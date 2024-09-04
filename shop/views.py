from django.shortcuts import render, redirect
from .models import Product, ProductTags, ProductCategory, ProductSubCategory
from blog.views import pagination
from django.contrib import messages


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

    return render(
        request=request,
        template_name="shop/shop.html",
        context={
            "title": "Shop",
            "img": "/media/page-title/shop.jpg",
            "pages": pagination(request=request, object_list=queryset, per_page=9),
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
        template_name="shop/products-by-tag.html",
        context={
            "title": tag.name,
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
        template_name="shop/products-by-category.html",
        context={
            "title": category.name,
            "img": "/media/page-title/shop.jpg",
            "pages": pagination(request=request,
                                object_list=queryset,
                                per_page=9)
        }
    )


# def products_by_subcategory(request, category_slug, subcategory_slug):
#     try:
#         category = ProductCategory.objects.get(slug=category_slug)
#         subcategory = ProductSubCategory.objects.get(slug=subcategory_slug, category=category)
#
#     except ProductCategory.DoesNotExist:
#         print("Category except")
#         messages.info(
#             request=request,
#             message=f"The category named '{category_slug.replace('-', ' ').title()}' does not exist.",
#         )
#
#         return redirect(to="shop")
#
#     except ProductSubCategory.DoesNotExist:
#         print("Subcategory except")
#         messages.info(
#             request=request,
#             message=f"The subcategory named '{subcategory_slug.replace('-', ' ').title()}' does not exist.",
#         )
#
#         return redirect(to="shop")
#
#     except (ProductCategory.DoesNotExist, ProductSubCategory.DoesNotExist):
#         messages.info(
#             request=request,
#             message=f"The specified category name '{category_slug.replace('-', ' ').title()}' and subcategory name '{subcategory_slug.replace('-', ' ').title()}' do not exist.",
#         )
#
#     queryset = Product.objects.filter(category=category, subcategory=subcategory, is_active=True)
#     queryset = sort_products(request=request, queryset=queryset)
#
#     return render(
#         request=request,
#         template_name="shop/products-by-subcategory.html",
#         context={
#             "title": subcategory.name,
#             "img": "/media/page-title/shop.jpg",
#             "pages": pagination(request=request,
#                                 object_list=queryset,
#                                 per_page=9)
#         }
#     )

def products_by_subcategory(request, category_slug, subcategory_slug):
    category_exists = False
    subcategory_exists = False

    try:
        print("Try 1")
        category = ProductCategory.objects.get(slug=category_slug)
        category_exists = True

    except ProductCategory.DoesNotExist:
        print("Except ProductCategory")
        category = None

    try:
        print("Try 2")
        if category:
            print("If Category")
            subcategory = ProductSubCategory.objects.get(category=category, slug=subcategory_slug)
            subcategory_exists = True

        else:
            print("No Category")
            subcategory = None

    except ProductSubCategory.DoesNotExist:
        print("Except Product SubCategory")
        subcategory = None

    if not category_exists and not subcategory_exists:
        print("Not Category and not SubCategory")
        messages.info(
            request=request,
            message=f"The specified category name '{category_slug.replace('-', ' ').title()}' and subcategory name '{subcategory_slug.replace('-', ' ').title()}' do not exist.",
        )

    elif not category_exists:
        print("Not Category")
        messages.info(
            request=request,
            message=f"The category named '{category_slug.replace('-', ' ').title()}' does not exist.",
        )

    elif not subcategory_exists:
        print("Not SubCategory")
        messages.info(
            request=request,
            message=f"The subcategory named '{subcategory_slug.replace('-', ' ').title()}' does not exist.",
        )

    if category_exists and subcategory_exists:
        print("If Category and SubCategory")
        queryset = Product.objects.filter(category=category, subcategory=subcategory, is_active=True)
        queryset = sort_products(request=request, queryset=queryset)

        return render(
            request=request,
            template_name="shop/products-by-subcategory.html",
            context={
                "title": subcategory.name,
                "img": "/media/page-title/shop.jpg",
                "pages": pagination(request=request,
                                    object_list=queryset,
                                    per_page=9)
            }
        )

    return redirect(to="shop")

    # try:
    #     category = ProductCategory.objects.get(slug=category_slug)
    #     subcategory = ProductSubCategory.objects.get(slug=subcategory_slug, category=category)
    #
    # except ProductCategory.DoesNotExist:
    #     print("Category except")
    #     messages.info(
    #         request=request,
    #         message=f"The category named '{category_slug.replace('-', ' ').title()}' does not exist.",
    #     )
    #
    #     return redirect(to="shop")
    #
    # except ProductSubCategory.DoesNotExist:
    #     print("Subcategory except")
    #     messages.info(
    #         request=request,
    #         message=f"The subcategory named '{subcategory_slug.replace('-', ' ').title()}' does not exist.",
    #     )
    #
    #     return redirect(to="shop")
    #
    # except (ProductCategory.DoesNotExist, ProductSubCategory.DoesNotExist):
    #     messages.info(
    #         request=request,
    #         message=f"The specified category name '{category_slug.replace('-', ' ').title()}' and subcategory name '{subcategory_slug.replace('-', ' ').title()}' do not exist.",
    #     )

    # queryset = Product.objects.filter(category=category, subcategory=subcategory, is_active=True)
    # queryset = sort_products(request=request, queryset=queryset)
    #
    # return render(
    #     request=request,
    #     template_name="shop/products-by-subcategory.html",
    #     context={
    #         "title": subcategory.name,
    #         "img": "/media/page-title/shop.jpg",
    #         "pages": pagination(request=request,
    #                             object_list=queryset,
    #                             per_page=9)
    #     }
    # )
