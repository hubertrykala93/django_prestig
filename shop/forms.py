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
    DeliveryDetails,
)


class DeliveryDetailsForm(forms.ModelForm):
    phone_number = forms.IntegerField(help_text="Provide your phone number.", label="Phone Number")
    country = forms.CharField(help_text="Provide the country.", label="Country")
    state = forms.CharField(help_text="Provide the state.", label="State")
    city = forms.CharField(help_text="Provide the city.", label="City")
    street = forms.CharField(help_text="Provide the street.", label="Street")
    house_number = forms.CharField(help_text="Provide the house number.", label="House Number")
    apartment_number = forms.CharField(help_text="Provide the apartment number.", label="Apartment Number",
                                       required=False)
    postal_code = forms.CharField(help_text="Provide the postal code.", label="Postal Code")

    def __init__(self, *args, **kwargs):
        super(DeliveryDetailsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = DeliveryDetails
        fields = "__all__"


class BrandForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the brand name.", label="Name")
    slug = forms.SlugField(required=False)
    description = forms.CharField(max_length=10000, help_text="Provide a brief description of the brand.",
                                  label="Description")
    logo = forms.ImageField(help_text="Upload the brand logo.", label="Logo")

    class Meta:
        model = Brand
        fields = "__all__"


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

    def __init__(self, *args, **kwargs):
        super(ProductCategoryForm, self).__init__(*args, **kwargs)

        self.fields["subcategory"].help_text = "Add a subcategory for this category."
        self.fields["subcategory"].label = "SubCategory"
        self.fields["subcategory"].required = False

    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductSubCategoryForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the subcategory name.", label="Name")
    slug = forms.SlugField(required=False)
    image = forms.ImageField(help_text="Upload an image for this subcategory.", label="Image")

    class Meta:
        model = ProductSubCategory
        fields = "__all__"


class SizeForm(forms.ModelForm):
    size = forms.CharField(help_text="Provide the size.", label="Size")

    class Meta:
        model = Size
        fields = "__all__"


class ColorForm(forms.ModelForm):
    color = forms.CharField(help_text="Provide the color.", label="Color")
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
    thumbnail = forms.ImageField(help_text="Upload a product thumbnail.", label="Thumbnail")
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
