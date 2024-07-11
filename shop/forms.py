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
    def __init__(self, *args, **kwargs):
        super(BrandForm, self).__init__(*args, **kwargs)

        self.fields["name"].help_text = "Provide the brand name."
        self.fields["description"].help_text = "Provide a brief description of the brand."
        self.fields["logo"].help_text = "Upload the brand logo."

        self.fields["name"].label = "Brand Name"
        self.fields["description"].label = "Brand Description"
        self.fields["logo"].label = "Brand Logo"

    class Meta:
        model = Brand
        fields = "__all__"


class ProductTagsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductTagsForm, self).__init__(*args, **kwargs)

        self.fields["name"].help_text = "Provide the tag name."

        self.fields["name"].label = "Tag Name"

    class Meta:
        model = ProductTags
        fields = "__all__"


class ProductCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductCategoryForm, self).__init__(*args, **kwargs)

        self.fields["name"].help_text = "Provide the category name."
        self.fields["image"].help_text = "Upload an image for this category."
        self.fields["subcategory"].help_text = "Add a subcategory for this category."
        self.fields["is_active"].help_text = "Indicate whether the category is active."

        self.fields["name"].label = "Category Name"
        self.fields["image"].label = "Category Image"
        self.fields["subcategory"].label = "Subcategory"

    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductSubCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductSubCategoryForm, self).__init__(*args, **kwargs)

        self.fields["name"].help_text = "Provide the subcategory name."
        self.fields["image"].help_text = "Upload an image for this subcategory."

        self.fields["name"].label = "Subcategory Name"
        self.fields["image"].label = "Subcategory Image"

    class Meta:
        model = ProductSubCategory
        fields = "__all__"


class SizeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SizeForm, self).__init__(*args, **kwargs)

        self.fields["size"].help_text = "Provide the size."

        self.fields["size"].label = "Product Size"

    class Meta:
        model = Size
        fields = "__all__"


class ColorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ColorForm, self).__init__(*args, **kwargs)

        self.fields["color"].help_text = "Provide the color."
        self.fields["hex"].help_text = "Provide the hex."

        self.fields["color"].label = "Product Color"
        self.fields["hex"].label = "Color Hex"

    class Meta:
        model = Color
        fields = "__all__"


class ProductGalleryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductGalleryForm, self).__init__(*args, **kwargs)

        self.fields["image"].help_text = "Upload an image for product."

    class Meta:
        model = ProductGallery
        fields = "__all__"


class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StockForm, self).__init__(*args, **kwargs)

        self.fields["quantity"].help_text = "Provide the quantity of the product."
        self.fields["color"].help_text = "Provide the color of the product."
        self.fields["size"].help_text = "Provide the size of the product."

        self.fields["quantity"].label = "Product Quantity"
        self.fields["color"].label = "Product Color"
        self.fields["size"].label = "Product Size"

    class Meta:
        model = Stock
        fields = "__all__"


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["brand"].help_text = "Provide or select the product brand."
        self.fields["category"].help_text = "Select the product category."
        self.fields["name"].help_text = "Provide the product name."
        self.fields["short_description"].help_text = "Provide a short description of the product."
        self.fields["price"].help_text = "Provide the product price."
        self.fields["quantity"].help_text = "Provide the quantity, and select the color and size of the product."
        self.fields["thumbnail"].help_text = "Upload a product thumbnail."
        self.fields["gallery"].help_text = "Upload a product image gallery or select images from the gallery."
        self.fields["tags"].help_text = "Provide or select the product tag(s)."
        self.fields["full_description"].help_text = "Provide a full description of the product."
        self.fields["is_active"].help_text = "Indicate if the product is active for sale."
        self.fields["is_featured"].help_text = "Indicate if you want to feature the product."

        self.fields["brand"].label = "Product Brand"
        self.fields["category"].label = "Product Category"
        self.fields["name"].label = "Product Name"
        self.fields["short_description"].label = "Product Short Description"
        self.fields["price"].label = "Product Price"
        self.fields["quantity"].label = "Product Quantity, Size and Color"
        self.fields["thumbnail"].label = "Product Thumbnail"
        self.fields["gallery"].label = "Product Gallery"
        self.fields["tags"].label = "Product Tags"
        self.fields["full_description"].label = "Product Full Description"

    class Meta:
        model = Product
        exclude = ["sales_counter", "rate"]
