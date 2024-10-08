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
    ProductReview,
    SizeGuideImage,
    ProductSpecification,
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
    ProductReviewForm,
    SizeGuideImageForm,
    ProductSpecificationForm,
)
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin


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


@admin.register(SizeGuideImage)
class AdminSizeGuideImage(admin.ModelAdmin):
    """
    Admin options and functionalities for SizeGuideImage model.
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
    form = SizeGuideImageForm
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


@admin.register(ProductSubCategory)
class AdminProductSubCategory(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductSubCategory model.
    """
    list_display = ["id", "name", "slug", "get_category_id", "get_category", "get_size_guide_id",
                    "get_size_guide_image_name", "is_active"]
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
            "Related Category", {
                "fields": [
                    "category",
                ],
            },
        ),
        (
            "Uploading", {
                "fields": [
                    "size_guide_image",
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

    def get_category_id(self, obj):
        return obj.category.id

    get_category_id.short_description = "Category ID"

    def get_category(self, obj):
        return obj.category.name

    get_category.short_description = "Category"

    def get_size_guide_id(self, obj):
        if obj.size_guide_image:
            return obj.size_guide_image.id

    get_size_guide_id.short_description = "Size Guide ID"

    def get_size_guide_image_name(self, obj):
        if obj.size_guide_image:
            return obj.size_guide_image.image.name

    get_size_guide_image_name.short_description = "Size Guide"


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


class StockInLine(admin.TabularInline):
    """
    Admin options and functionalities for Stock model.
    """
    model = Stock
    extra = 1
    form = StockForm


@admin.register(Stock)
class AdminStock(admin.ModelAdmin):
    """
    Admin options and functionalities for Stock model.
    """
    model = Stock
    extra = 1
    list_display = ["id", "get_product_id", "product", "quantity", "get_size_id", "size", "get_color_id", "color"]
    form = StockForm
    fieldsets = (
        (
            "Product", {
                "fields": [
                    "product",
                ],
            },
        ),
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

    def get_product_id(self, obj):
        return obj.product.id

    get_product_id.short_description = "Product ID"

    def get_size_id(self, obj):
        return obj.size.id

    get_size_id.short_description = "Size ID"

    def get_color_id(self, obj):
        return obj.color.id

    get_color_id.short_description = "Color ID"


@admin.register(Product)
class AdminProduct(SummernoteModelAdmin):
    """
    Admin options and functionalities for Product model.
    """
    list_display = [
        "id",
        "uuid",
        "formatted_created_at",
        "get_brand_id",
        "brand",
        "get_category_id",
        "category",
        "get_subcategory_id",
        "subcategory",
        "name",
        "slug",
        "short_description",
        "price",
        "get_gallery_ids",
        "get_gallery",
        "get_tags_ids",
        "get_tags",
        "sku",
        "is_active",
        "is_featured",
        "sales_counter",
        "product_specification",
    ]
    form = ProductForm
    fieldsets = (
        (
            "Basic Information", {
                "fields": [
                    "brand",
                    "category",
                    "subcategory",
                    "tags",
                    "name",
                    "price",
                    "short_description",
                    "full_description",
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
        (
            "Specification", {
                "fields": [
                    "product_specification",
                ],
            },
        ),
    )
    inlines = [StockInLine]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'subcategory':
            category_id = request.POST.get('category') or request.GET.get('category')

            if category_id:
                try:
                    category = ProductCategory.objects.get(id=category_id)
                    kwargs["queryset"] = ProductSubCategory.objects.filter(category=category)

                except ProductCategory.DoesNotExist:
                    kwargs["queryset"] = ProductSubCategory.objects.none()

        return super(AdminProduct, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def formatted_created_at(self, obj):
        if obj.created_at:
            return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"

    def get_brand_id(self, obj):
        return obj.brand.id

    get_brand_id.short_description = "Brand ID"

    def get_category_id(self, obj):
        return obj.category.id

    get_category_id.short_description = "Category ID"

    def get_subcategory_id(self, obj):
        return obj.subcategory.id

    get_subcategory_id.short_description = "Subcategory ID"

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


@admin.register(ProductReview)
class AdminProductReview(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductReview model.
    """
    list_display = [
        "id",
        "formatted_created_at",
        "get_user_id",
        "user",
        "get_product_id",
        "product",
        "content",
        "rate",
    ]
    form = ProductReviewForm
    fieldsets = (
        (
            "Author", {
                "fields": [
                    "user",
                ],
            },
        ),
        (
            "Reviewing Product", {
                "fields": [
                    "product",
                ],
            },
        ),
        (
            "Review Content", {
                "fields": [
                    "content",
                ],
            },
        ),
        (
            "Rate", {
                "fields": [
                    "rate",
                ],
            },
        ),
    )

    def formatted_created_at(self, obj):
        if obj.created_at:
            return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"

    def get_user_id(self, obj):
        return obj.user.id

    get_user_id.short_description = "User ID"

    def get_product_id(self, obj):
        return obj.product.id

    get_product_id.short_description = "Product ID"


@admin.register(ProductSpecification)
class AdminProductSpecification(admin.ModelAdmin):
    """
    Admin options and functionalities for ProductSpecification model.
    """
    list_display = [
        "size_guide_image",
        "made_in",
        "washing_temperature",
        "material",
        "composition",
        "chest",
        "shoulder",
        "waist",
        "hip",
        "sleeve",
        "length",
        "width",
        "inches",
        "knee",
        "leg_opening",
    ]
    form = ProductSpecificationForm
    fieldsets = (
        (
            "General", {
                "fields": [
                    "made_in",
                    "washing_temperature",
                    "material",
                    "composition",
                ]
            },
        ),
        (
            "Sizes", {
                "fields": [
                    "chest",
                    "shoulder",
                    "waist",
                    "hip",
                    "sleeve",
                    "length",
                    "width",
                    "inches",
                    "knee",
                    "leg_opening",
                ],
            },
        ),
        (
            "Uploading", {
                "fields": [
                    "size_guide_image",
                ],
            },
        ),
    )
