from django import forms
from .models import (
    Brand,
    ProductTags,
    ProductCategory,
    ProductSubCategory,
    Size,
    Color,
    ProductImage,
    Stock,
    Product,
    BrandLogo,
    ProductCategoryImage,
    ProductReview,
)


class BrandLogoForm(forms.ModelForm):
    size = forms.IntegerField(required=False)
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)
    format = forms.CharField(required=False)
    alt = forms.CharField(help_text="Provide the alternate text.", label="Alt", required=True, widget=forms.Textarea)

    class Meta:
        model = BrandLogo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BrandLogoForm, self).__init__(*args, **kwargs)
        self.fields["image"].help_text = "Upload image to the brand."
        self.fields["image"].label = "Logo"
        self.fields["image"].required = True


class BrandForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the brand name.", label="Name")
    slug = forms.SlugField(required=False)
    description = forms.CharField(max_length=10000, help_text="Provide a brief description of the brand.",
                                  label="Description", widget=forms.Textarea)

    class Meta:
        model = Brand
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BrandForm, self).__init__(*args, **kwargs)

        self.fields["logo"].help_text = "Choose the brand logo."
        self.fields["logo"].label = "Logo"
        self.fields["logo"].required = True


class ProductTagsForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the tag name.", label="Name")
    slug = forms.SlugField(required=False)

    class Meta:
        model = ProductTags
        fields = "__all__"


class ProductCategoryImageForm(forms.ModelForm):
    size = forms.IntegerField(required=False)
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)
    format = forms.CharField(required=False)
    alt = forms.CharField(help_text="Provide the alternate text.", label="Alt", required=True, widget=forms.Textarea)

    class Meta:
        model = ProductCategoryImage
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductCategoryImageForm, self).__init__(*args, **kwargs)

        self.fields["image"].help_text = "Upload an image to the product category."
        self.fields["image"].label = "Image"
        self.fields["image"].required = True


class ProductCategoryForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the category name.", label="Name")
    slug = forms.SlugField(required=False)
    is_active = forms.BooleanField(help_text="Indicate whether the category is active.", required=False)

    class Meta:
        model = ProductCategory
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductCategoryForm, self).__init__(*args, **kwargs)

        self.fields["category_image"].help_text = "Choose the category image."
        self.fields["category_image"].label = "Image"
        self.fields["category_image"].required = True


class ProductSubCategoryForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the subcategory name.", label="Name")
    slug = forms.SlugField(required=False)
    is_active = forms.BooleanField(help_text="Indicate whether the subcategory is active.", required=False)

    class Meta:
        model = ProductSubCategory
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductSubCategoryForm, self).__init__(*args, **kwargs)

        self.fields["category"].help_text = "Add a category for this subcategory."
        self.fields["category"].label = "Category"
        self.fields["category"].required = True


class SizeForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the size.", label="Size")

    class Meta:
        model = Size
        fields = "__all__"


class ColorForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the color name.", label="Name")
    hex = forms.CharField(help_text="Provide the hex.", label="Hex")

    class Meta:
        model = Color
        fields = "__all__"


class StockForm(forms.ModelForm):
    quantity = forms.IntegerField(help_text="Provide the quantity of the product.", label="Quantity")

    def __init__(self, *args, **kwargs):
        super(StockForm, self).__init__(*args, **kwargs)

        self.fields["color"].help_text = "Provide the color of the product."
        self.fields["size"].help_text = "Provide the size of the product."

        self.fields["color"].label = "Color"
        self.fields["size"].label = "Size"

    class Meta:
        model = Stock
        fields = "__all__"


class ProductImageForm(forms.ModelForm):
    size = forms.IntegerField(required=False)
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)
    format = forms.CharField(required=False)
    alt = forms.CharField(help_text="Provide the alternate text.", label="Alt", required=True, widget=forms.Textarea)
    is_featured = forms.BooleanField(help_text="Check if you want to highlight this photo.", required=False)

    class Meta:
        model = ProductImage
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductImageForm, self).__init__(*args, **kwargs)

        self.fields["image"].help_text = "Upload an image to the product."
        self.fields["image"].label = "Image"
        self.fields["image"].required = True


class ProductForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the product name.", label="Name")
    slug = forms.SlugField(required=False)
    short_description = forms.CharField(help_text="Provide a short description of the product.",
                                        label="Short Description", widget=forms.Textarea)
    price = forms.FloatField(help_text="Provide the product price.", label="Price")
    full_description = forms.CharField(max_length=100000, help_text="Provide a full description of the product.",
                                       label="Full Description", widget=forms.Textarea)
    is_active = forms.BooleanField(help_text="Indicate if the product is active for sale.", required=False)
    is_featured = forms.BooleanField(help_text="Indicate if you want to feature the product.", required=False)

    class Meta:
        model = Product
        exclude = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["brand"].help_text = "Provide or select the product brand."
        self.fields["category"].help_text = "Select the product category."
        self.fields["subcategory"].help_text = "Select the product subcategory."
        self.fields["quantity"].help_text = "Provide the quantity, and select the color and size of the product."
        self.fields["gallery"].help_text = "Upload a product image gallery or select images from the gallery."
        self.fields["tags"].help_text = "Provide or select the product tag(s)."

        self.fields["brand"].label = "Brand"
        self.fields["category"].label = "Category"
        self.fields["subcategory"].label = "Subcategory"
        self.fields["quantity"].label = "Quantity, Size and Color"
        self.fields["gallery"].label = "Gallery"
        self.fields["tags"].label = "Tags"

        self.fields["tags"].required = False
        self.fields["gallery"].required = True

        if "category" in self.data:
            category_id = self.data.get(key="category")

            if category_id.isdigit():
                try:
                    category = ProductCategory.objects.get(id=category_id)
                    self.fields["subcategory"].queryset = ProductSubCategory.objects.filter(category=category)

                except ProductCategory.DoesNotExist:
                    self.fields["subcategory"].queryset = ProductSubCategory.objects.none()

            else:
                self.fields["subcategory"].queryset = ProductSubCategory.objects.all()

        elif self.instance.pk:
            if self.instance.category:
                self.fields["subcategory"].queryset = ProductSubCategory.objects.filter(category=self.instance.category)

            else:
                self.fields["subcategory"].queryset = ProductSubCategory.objects.none()


class ProductReviewForm(forms.ModelForm):
    content = forms.CharField(help_text="Provide the content of the review.", label="Content", required=True,
                              widget=forms.Textarea)
    rate = forms.IntegerField(help_text="Provide the rate of the product.", label="Rate", required=True)

    class Meta:
        model = ProductReview
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductReviewForm, self).__init__(*args, **kwargs)

        self.fields["user"].help_text = "Select the author of the review."
        self.fields["user"].label = "Author"
        self.fields["user"].required = True

        self.fields["product"].help_text = "Select the reviewing product."
        self.fields["product"].label = "Product"
        self.fields["product"].required = True
