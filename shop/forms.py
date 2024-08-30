from django import forms
from .models import (
    Brand,
    ProductTags,
    ProductCategory,
    ProductSubCategory,
    Size,
    Color,
    ProductGallery,
    Stock,
    Product,
    BrandLogo,
)


class BrandLogoForm(forms.ModelForm):
    size = forms.IntegerField(required=False)
    width = forms.IntegerField(required=False)
    height = forms.IntegerField(required=False)
    format = forms.CharField(required=False)

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


class ProductCategoryForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the category name.", label="Name")
    slug = forms.SlugField(required=False)
    image = forms.ImageField(help_text="Upload an image for this category.", label="Image")
    is_active = forms.BooleanField(help_text="Indicate whether the category is active.", required=False)

    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductSubCategoryForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the subcategory name.", label="Name")
    slug = forms.SlugField(required=False)
    image = forms.ImageField(help_text="Upload an image for this subcategory.", label="Image")
    is_active = forms.BooleanField(help_text="Indicate whether the category is active.", required=False)

    class Meta:
        model = ProductSubCategory
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductSubCategoryForm, self).__init__(*args, **kwargs)

        self.fields["categories"].help_text = "Add a category for this subcategory."
        self.fields["categories"].label = "Category"
        self.fields["categories"].required = False


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


class ProductGalleryForm(forms.ModelForm):
    image = forms.ImageField(help_text="Upload an image for product.", label="Product Image")

    class Meta:
        model = ProductGallery
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


class ProductForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the product name.", label="Name")
    slug = forms.SlugField(required=False)
    short_description = forms.CharField(help_text="Provide a short description of the product.",
                                        label="Short Description")
    price = forms.FloatField(help_text="Provide the product price.", label="Price")
    image = forms.ImageField(help_text="Upload a product thumbnail.", label="Thumbnail")
    full_description = forms.CharField(max_length=100000, help_text="Provide a full description of the product.",
                                       label="Full Description")
    is_active = forms.BooleanField(help_text="Indicate if the product is active for sale.", required=False)
    is_featured = forms.BooleanField(help_text="Indicate if you want to feature the product.", required=False)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["brand"].help_text = "Provide or select the product brand."
        self.fields["category"].help_text = "Select the product category."
        self.fields["quantity"].help_text = "Provide the quantity, and select the color and size of the product."
        self.fields["gallery"].help_text = "Upload a product image gallery or select images from the gallery."
        self.fields["tags"].help_text = "Provide or select the product tag(s)."
        self.fields["tags"].required = False

        self.fields["brand"].label = "Brand"
        self.fields["category"].label = "Category"
        self.fields["quantity"].label = "Quantity, Size and Color"
        self.fields["gallery"].label = "Gallery"
        self.fields["tags"].label = "Tags"

    class Meta:
        model = Product
        exclude = ["sales_counter", "rate"]
