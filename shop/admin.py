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
    ProductImage,
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
    ProductImageForm,
    StockForm,
    ProductForm,
    BrandLogoForm,
    ProductCategoryImageForm,
    ProductSubCategoryImageForm,
)
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe


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
        "alt",
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
        (
            "Alternate Text", {
                "fields": [
                    "alt",
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
        "alt",
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
        (
            "Alternate Text", {
                "fields": [
                    "alt",
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

    formatted_updated_at.short_description = "Updated At"

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
    list_display = ["id", "formatted_created_at", "formatted_updated_at", "image", "get_image_name", "size", "width",
                    "height", "format", "alt"]
    form = ProductSubCategoryImageForm
    fieldsets = (
        (
            "Uploading", {
                "fields": [
                    "image",
                ],
            },
        ),
        (
            "Alternate Text", {
                "fields": [
                    "alt",
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

    formatted_updated_at.short_description = "Updated At"

    def get_image_name(self, obj):
        if obj.image:
            return obj.image.name.split(sep="/")[-1]

    get_image_name.short_description = "Image Name"


@admin.register(ProductSubCategory)
class AdminProductSubCategory(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductSubCategory model.
    """
    list_display = ["id", "name", "slug", "get_subcategory_image_id", "get_subcategory_image_name", "is_active"]
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

    def get_subcategory_image_id(self, obj):
        if obj.subcategory_image:
            return obj.subcategory_image

    get_subcategory_image_id.short_description = "Subcategory Image ID"

    def get_subcategory_image_name(self, obj):
        if obj.subcategory_image:
            return obj.subcategory_image.image.name.split(sep="/")[-1]

    get_subcategory_image_name.short_Description = "Subcategory Image Name"


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


@admin.register(ProductImage)
class AdminProductImage(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductImage model.
    """
    list_display = ["id", "formatted_created_at", "formatted_updated_at", "image", "get_image_name", "size", "width",
                    "height", "format", "alt", "is_featured"]
    form = ProductImageForm
    fieldsets = (
        (
            "Uploading", {
                "fields": [
                    "image",
                ],
            },
        ),
        (
            "Altenate Text", {
                "fields": [
                    "alt",
                ],
            },
        ),
        (
            "Featured", {
                "fields": [
                    "is_featured",
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

    formatted_updated_at.short_description = "Updated At"

    def get_image_name(self, obj):
        if obj.image:
            return obj.image.name.split(sep="/")[-1]

    get_image_name.short_description = "Image Name"


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
        "formatted_created_at",
        "brand",
        "category",
        "name",
        "slug",
        "short_description",
        "price",
        "get_quantity",
        "get_gallery_ids",
        "get_gallery",
        "rate",
        "get_tags_ids",
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

    def formatted_created_at(self, obj):
        if obj.created_at:
            return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"

    def get_gallery_ids(self, obj):
        return format_html_join(
            mark_safe('<br>'),
            '{}',
            ((img.id,) for img in obj.gallery.all())
        ) or mark_safe("-")

    get_gallery_ids.short_description = "Gallery ID"

    def get_gallery(self, obj):
        return format_html_join(
            mark_safe('<br>'),
            '{}',
            ((img.image,) for img in obj.gallery.all())
        ) or mark_safe("-")

    get_gallery.short_description = "Gallery"

    def get_quantity(self, obj):
        return "\n".join([" ".join([str(s.quantity), s.size.name, s.color.name]) for s in obj.quantity.all()])

    get_quantity.short_description = "Quantity"

    def get_tags(self, obj):
        return format_html_join(
            mark_safe('<br>'),
            '{}',
            ((tag.name,) for tag in obj.tags.all())
        ) or mark_safe("-")

    get_tags.short_description = "Tags"

    def get_tags_ids(self, obj):
        return format_html_join(
            mark_safe('<br>'),
            '{}',
            ((tag.id,) for tag in obj.tags.all())
        ) or mark_safe("-")

    get_tags_ids.short_description = "Tag ID"
