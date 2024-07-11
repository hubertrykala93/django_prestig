from django.contrib import admin
from .models import (
    Brand,
    ProductTags,
    ProductCategory,
    ProductSubCategory,
    Product,
    Color,
    Size,
    Stock,
    ProductGallery
)
from .forms import (
    BrandForm,
    ProductTagsForm,
    ProductCategoryForm,
    ProductSubCategoryForm,
    ColorForm,
    SizeForm,
    ProductGalleryForm,
    StockForm,
    ProductForm
)


@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    """
    Admin options and functionalities for Brand model.
    """
    fields = ["name", "slug", "description", "logo"]
    list_display = ["id", "name", "slug", "description", "logo"]
    list_editable = ["slug"]
    prepopulated_fields = {"slug": ["name"]}
    form = BrandForm


@admin.register(ProductTags)
class AdminProductTags(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductTags model.
    """
    fields = ["name", "slug"]
    list_display = ["id", "name", "slug"]
    list_editable = ["slug"]
    prepopulated_fields = {"slug": ["name"]}
    form = ProductTagsForm


@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductCategory model.
    """
    fields = ["name", "slug", "image", "subcategory", "is_active"]
    list_display = ["id", "name", "slug", "image", "subcategory", "is_active"]
    prepopulated_fields = {"slug": ["name"]}
    form = ProductCategoryForm


@admin.register(ProductSubCategory)
class AdminProductSubCategory(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductSubCategory model.
    """
    fields = ["name", "slug", "image"]
    list_display = ["id", "name", "slug", "image"]
    prepopulated_fields = {"slug": ["name"]}
    form = ProductSubCategoryForm


@admin.register(Size)
class AdminSize(admin.ModelAdmin):
    """
    Admin options and functionalities for Size model.
    """
    fields = ["size"]
    list_display = ["id", "size"]
    form = SizeForm


@admin.register(Color)
class AdminColor(admin.ModelAdmin):
    """
    Admin options and functionalities for Color model.
    """
    fields = ["color", "hex"]
    list_display = ["id", "color", "hex"]
    form = ColorForm


@admin.register(ProductGallery)
class AdminProductGallery(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductGallery model.
    """
    fields = ["image"]
    list_display = ["id", "image"]
    form = ProductGalleryForm


@admin.register(Stock)
class AdminStock(admin.ModelAdmin):
    """
    Admin options and functionalities for Stock model.
    """
    fields = ["quantity", "size", "color"]
    list_display = ["id", "quantity", "size", "color"]
    form = StockForm


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    """
    Admin options and functionalities for Product model.
    """
    fields = [
        "brand",
        "category",
        "name",
        "slug",
        "short_description",
        "price",
        "quantity",
        "thumbnail",
        "gallery",
        "tags",
        "full_description",
        "is_active",
        "is_featured",
    ]
    list_display = [
        "id",
        "uuid",
        "created_at",
        "brand",
        "category",
        "name",
        "slug",
        "short_description",
        "price",
        "get_quantity",
        "thumbnail",
        "get_gallery",
        "rate",
        "get_tags",
        "full_description",
        "sku",
        "is_active",
        "is_featured",
        "sales_counter",
    ]
    form = ProductForm

    def get_gallery(self, obj):
        return "\n".join([g.image.name.split("/")[-1] for g in obj.gallery.all()])

    def get_quantity(self, obj):
        return "\n".join([" ".join([str(s.quantity), s.size.size, s.color.color]) for s in obj.quantity.all()])

    def get_tags(self, obj):
        return "\n".join([t.name for t in obj.tags.all()])
