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
    BrandLogo,
    ProductCategoryImage,
    ProductSubCategoryImage,
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
    BrandLogoForm,
    ProductCategoryImageForm,
    ProductSubCategoryImageForm,
)


@admin.register(BrandLogo)
class AdminBrandLogo(admin.ModelAdmin):
    """
    Admin options and functionalities for BrandLogo model.
    """
    list_display = [
        "id",
        "formatted_created_at",
        "formatted_updated_at",
        "image",
        "get_image_name",
        "size",
        "width",
        "height",
        "format",
    ]
    form = BrandLogoForm
    fieldsets = (
        (
            "Uploading", {
                "fields": [
                    "image",
                ],
            },
        ),
    )

    def formatted_created_at(self, obj):
        if obj.created_at:
            return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"

    def formatted_updated_at(self, obj):
        if obj.updated_at:
            return obj.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_updated_at.description = "Updated At"

    def get_image_name(self, obj):
        if obj.image:
            return obj.image.name.split("/")[-1]

    get_image_name.short_description = "Image Name"


@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    """
    Admin options and functionalities for Brand model.
    """
    list_display = [
        "id",
        "name",
        "slug",
        "description",
        "get_logo",
        "get_logo_name",
    ]
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

    def get_logo(self, obj):
        if obj.logo:
            return obj.logo

    get_logo.short_description = "Logo ID"

    def get_logo_name(self, obj):
        if obj.logo:
            return obj.logo.image

    get_logo_name.short_description = "Logo"


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


@admin.register(ProductCategoryImage)
class AdminProductCategoryImage(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductCategoryImage model.
    """
    list_display = [
        "id",
        "formatted_created_at",
        "formatted_updated_at",
        "image",
        "get_image_name",
        "size",
        "width",
        "height",
        "format",
    ]
    form = ProductCategoryImageForm
    fieldsets = (
        (
            "Uploading", {
                "fields": [
                    "image",
                ],
            },
        ),
    )

    def formatted_created_at(self, obj):
        if obj.created_at:
            return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"

    def formatted_updated_at(self, obj):
        if obj.updated_at:
            return obj.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_updated_at.description = "Updated At"

    def get_image_name(self, obj):
        if obj.image:
            return obj.image.name.split("/")[-1]

    get_image_name.short_description = "Image Name"


@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductCategory model.
    """
    list_display = ["id", "name", "slug", "get_category_image_id", "get_category_image", "is_active"]
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
                    "category_image",
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

    def get_category_image_id(self, obj):
        if obj.category_image:
            return obj.category_image

    get_category_image_id.short_description = "Category Image ID"

    def get_category_image(self, obj):
        if obj.category_image:
            return obj.category_image.image

    get_category_image.short_description = "Category Image"


@admin.register(ProductSubCategoryImage)
class AdminProductSubCategoryImage(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductSubCategoryImage model.
    """
    list_display = ["id", "created_at", "updated_at", "image", "size", "width", "height", "format"]
    form = ProductSubCategoryImageForm
    fieldsets = (
        (
            "Uploading", {
                "fields": [
                    "image",
                ],
            },
        ),
    )


@admin.register(ProductSubCategory)
class AdminProductSubCategory(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductSubCategory model.
    """
    list_display = ["id", "name", "slug", "subcategory_image", "is_active"]
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
                    "subcategory_image",
                ],
            },
        ),
        (
            "Related Category", {
                "fields": [
                    "categories",
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


@admin.register(Size)
class AdminSize(admin.ModelAdmin):
    """
    Admin options and functionalities for Size model.
    """
    list_display = ["id", "name"]
    form = SizeForm
    fieldsets = (
        (
            "Basic Information", {
                "fields": [
                    "name",
                ],
            },
        ),
    )


@admin.register(Color)
class AdminColor(admin.ModelAdmin):
    """
    Admin options and functionalities for Color model.
    """
    list_display = ["id", "name", "hex"]
    form = ColorForm
    fieldsets = (
        (
            "Basic Information", {
                "fields": [
                    "name",
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
        "image",
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
                    "image",
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
