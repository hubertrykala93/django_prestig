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
    Product
)


class BrandForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the brand name.", label="Brand Name")
    slug = forms.SlugField(help_text="It will be created automatically.")
    description = forms.CharField(max_length=10000, help_text="Provide a brief description of the brand.",
                                  label="Brand Description")
    logo = forms.ImageField(help_text="Upload the brand logo.", label="Brand Logo")

    class Meta:
        model = Brand
        fields = "__all__"


class ProductTagsForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the tag name.", label="Tag Name")
    slug = forms.SlugField(help_text="It will be created automatically.")

    class Meta:
        model = ProductTags
        fields = "__all__"


class ProductCategoryForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the category name.", label="Category Name")
    image = forms.ImageField(help_text="Upload an image for this category.", label="Category Image")
    is_active = forms.BooleanField(help_text="Indicate whether the category is active.")

    def __init__(self, *args, **kwargs):
        super(ProductCategoryForm, self).__init__(*args, **kwargs)

        self.fields["subcategory"].help_text = "Add a subcategory for this category."
        self.fields["subcategory"].label = "Subcategory"

    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductSubCategoryForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the subcategory name.", label="Subcategory Name")
    slug = forms.SlugField(help_text="It will be created automatically.")
    image = forms.ImageField(help_text="Upload an image for this subcategory.", label="Subcategory Image")

    class Meta:
        model = ProductSubCategory
        fields = "__all__"


class SizeForm(forms.ModelForm):
    size = forms.CharField(help_text="Provide the size.", label="Product Size")

    class Meta:
        model = Size
        fields = "__all__"


class ColorForm(forms.ModelForm):
    color = forms.CharField(help_text="Provide the color.", label="Product Color")
    hex = forms.CharField(help_text="Provide the hex.", label="Color Hex")

    class Meta:
        model = Color
        fields = "__all__"


class ProductGalleryForm(forms.ModelForm):
    image = forms.ImageField(help_text="Upload an image for product.", label="Product Image")

    class Meta:
        model = ProductGallery
        fields = "__all__"


class StockForm(forms.ModelForm):
    quantity = forms.IntegerField(help_text="Provide the quantity of the product.", label="Product Quantity")

    def __init__(self, *args, **kwargs):
        super(StockForm, self).__init__(*args, **kwargs)

        self.fields["color"].help_text = "Provide the color of the product."
        self.fields["size"].help_text = "Provide the size of the product."

        self.fields["color"].label = "Product Color"
        self.fields["size"].label = "Product Size"

    class Meta:
        model = Stock
        fields = "__all__"


class ProductForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the product name.", label="Product Name")
    slug = forms.SlugField(help_text="It will be created automatically.")
    short_description = forms.CharField(help_text="Provide a short description of the product.",
                                        label="Product Short Description")
    price = forms.FloatField(help_text="Provide the product price.", label="Product Price")
    thumbnail = forms.ImageField(help_text="Upload a product thumbnail.", label="Product Thumbnail")
    full_description = forms.CharField(max_length=100000, help_text="Provide a full description of the product.",
                                       label="Product Full Description")
    is_active = forms.BooleanField(help_text="Indicate if the product is active for sale.")
    is_featured = forms.BooleanField(help_text="Indicate if you want to feature the product.")

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["brand"].help_text = "Provide or select the product brand."
        self.fields["category"].help_text = "Select the product category."
        self.fields["quantity"].help_text = "Provide the quantity, and select the color and size of the product."
        self.fields["gallery"].help_text = "Upload a product image gallery or select images from the gallery."
        self.fields["tags"].help_text = "Provide or select the product tag(s)."

        self.fields["brand"].label = "Product Brand"
        self.fields["category"].label = "Product Category"
        self.fields["quantity"].label = "Product Quantity, Size and Color"
        self.fields["gallery"].label = "Product Gallery"
        self.fields["tags"].label = "Product Tags"
        self.fields["full_description"].label = "Product Full Description"

    class Meta:
        model = Product
        exclude = ["sales_counter", "rate"]
