from shop.models import ProductCategory, ProductSubCategory, Size, Color, Brand, ProductReview
from django.db.models import Count, Prefetch


def shop_filters(request):
    return {
        "categories": ProductCategory.objects.filter(is_active=True).annotate(
            product_count=Count('product')
        ).prefetch_related(
            Prefetch('subcategories', queryset=ProductSubCategory.objects.filter(is_active=True))
        ).order_by("-name"),
        "sizes": Size.objects.all(),
        "colors": Color.objects.all().order_by("-name"),
        "brands": Brand.objects.all().order_by("name"),
        "rates": ProductReview.objects.values_list("rate", flat=True).distinct(),
    }
