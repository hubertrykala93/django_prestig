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
    ProductGallery,
    DeliveryDetails,
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
    ProductForm,
    DeliveryDetailsForm,
)


@admin.register(DeliveryDetails)
class AdminDeliveryDetails(admin.ModelAdmin):
    """
    Admin options and functionalities for DeliveryDetails model.
    """
    list_display = ["id", "uuid", "country", "state", "city", "street", "get_house_number",
                    "get_apartment_number", "get_postal_code", "phone"]
    form = DeliveryDetailsForm
    fieldsets = (
        (
            "Contact Information", {
                "fields": [
                    "phone",
                ],
            },
        ),
        (
            "Shipping Address", {
                "fields": [
                    "country",
                    "state",
                    "city",
                    "street",
                    "housenumber",
                    "apartmentnumber",
                    "postalcode",
                ],
            },
        ),
    )

    def get_house_number(self, obj):
        return obj.housenumber

    get_house_number.short_description = "House Number"

    def get_apartment_number(self, obj):
        return obj.apartmentnumber

    get_apartment_number.short_description = "Apartment Number"

    def get_postal_code(self, obj):
        return obj.postalcode

    get_postal_code.short_description = "Postal Code"


@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    """
    Admin options and functionalities for Brand model.
    """
    list_display = ["id", "name", "slug", "description", "logo"]
    list_editable = ["slug"]
    prepopulated_fields = {"slug": ["name"]}
    form = BrandForm
    fieldsets = (
        (
            "Basic Information", {
                "fields": [
                    "name",
                    "description",
                ],
            },
        ),
        (
            "Uploading", {
                "fields": [
                    "logo",
                ],
            },
        ),
    )


@admin.register(ProductTags)
class AdminProductTags(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductTags model.
    """
    list_display = ["id", "name", "slug"]
    list_editable = ["slug"]
    prepopulated_fields = {"slug": ["name"]}
    form = ProductTagsForm
    fieldsets = (
        (
            "Basic Information", {
                "fields": [
                    "name",
                ],
            },
        ),
    )


@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductCategory model.
    """
    list_display = ["id", "name", "slug", "image", "get_subcategories", "is_active"]
    prepopulated_fields = {"slug": ["name"]}
    form = ProductCategoryForm
    fieldsets = (
        (
            "Basic Information", {
                "fields": [
                    "name",
                ],
            },
        ),
        (
            "Uploading", {
                "fields": [
                    "image",
                ],
            },
        ),
        (
            "Related SubCategory", {
                "fields": [
                    "subcategory",
                ],
            },
        ),
        (
            "Permissions", {
                "fields": [
                    "is_active",
                ],
            },
        ),
    )

    def get_subcategories(self, obj):
        return "\n".join([s.name for s in obj.subcategory.all()])


@admin.register(ProductSubCategory)
class AdminProductSubCategory(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductSubCategory model.
    """
    list_display = ["id", "name", "slug", "image"]
    prepopulated_fields = {"slug": ["name"]}
    form = ProductSubCategoryForm
    fieldsets = (
        (
            "Basic Information", {
                "fields": [
                    "name",
                ],
            },
        ),
        (
            "Uploading", {
                "fields": [
                    "image",
                ],
            },
        ),
    )


@admin.register(Size)
class AdminSize(admin.ModelAdmin):
    """
    Admin options and functionalities for Size model.
    """
    list_display = ["id", "size"]
    form = SizeForm
    fieldsets = (
        (
            "Basic Information", {
                "fields": [
                    "size",
                ],
            },
        ),
    )


@admin.register(Color)
class AdminColor(admin.ModelAdmin):
    """
    Admin options and functionalities for Color model.
    """
    list_display = ["id", "color", "hex"]
    form = ColorForm
    fieldsets = (
        (
            "Basic Information", {
                "fields": [
                    "color",
                    "hex",
                ],
            },
        ),
    )


@admin.register(ProductGallery)
class AdminProductGallery(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductGallery model.
    """
    list_display = ["id", "image"]
    form = ProductGalleryForm
    fieldsets = (
        (
            "Uploading", {
                "fields": [
                    "image",
                ],
            },
        ),
    )


@admin.register(Stock)
class AdminStock(admin.ModelAdmin):
    """
    Admin options and functionalities for Stock model.
    """
    list_display = ["id", "quantity", "size", "color"]
    form = StockForm
    fieldsets = (
        (
            "Product Quantity", {
                "fields": [
                    "quantity",
                ],
            },
        ),
        (
            "Product Details", {
                "fields": [
                    "size",
                    "color",
                ],
            },
        ),
    )


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    """
    Admin options and functionalities for Product model.
    """
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
    fieldsets = (
        (
            "Basic Information", {
                "fields": [
                    "brand",
                    "category",
                    "tags",
                    "name",
                    "price",
                    "short_description",
                    "full_description",
                    "quantity",
                ],
            },
        ),
        (
            "Uploading", {
                "fields": [
                    "thumbnail",
                    "gallery",
                ],
            },
        ),
        (
            "Permissions", {
                "fields": [
                    "is_active",

                ],
            },
        ),
        (
            "Additional", {
                "fields": [
                    "is_featured",
                ],
            },
        ),
    )

    def get_gallery(self, obj):
        return "\n".join([g.image.name.split("/")[-1] for g in obj.gallery.all()])

    def get_quantity(self, obj):
        return "\n".join([" ".join([str(s.quantity), s.size.size, s.color.color]) for s in obj.quantity.all()])

    def get_tags(self, obj):
        return "\n".join([t.name for t in obj.tags.all()])
