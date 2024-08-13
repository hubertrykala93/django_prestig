from django.db import models
from uuid import uuid4
from django.utils.timezone import now
from django.utils.text import slugify


class DeliveryDetails(models.Model):
    uuid = models.UUIDField(default=uuid4)
    phone = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=56)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=169)
    street = models.CharField(max_length=50)
    housenumber = models.CharField(max_length=5)  # Include the house number if the delivery is to a residential home
    apartmentnumber = models.CharField(max_length=5)  # Include the apartment number if the delivery is to a building with multiple units
    postalcode = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Delivery Detail"
        verbose_name_plural = "Delivery Details"

    def __str__(self):
        return str(self.uuid)


class Brand(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=10000)
    logo = models.ImageField(upload_to='shop/brands')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(Brand, self).save(*args, **kwargs)


class ProductTags(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Product Tag"
        verbose_name_plural = "Product Tags"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(ProductTags, self).save(*args, **kwargs)


class ProductSubCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField(upload_to='shop/subcategories')

    class Meta:
        verbose_name = "Product SubCategory"
        verbose_name_plural = "Product SubCategories"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(ProductSubCategory, self).save(*args, **kwargs)


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='shop/categories')
    subcategory = models.ManyToManyField(to=ProductSubCategory)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(ProductCategory, self).save(*args, **kwargs)


class Size(models.Model):
    size = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    def __str__(self):
        return f"{self.size}"


class Color(models.Model):
    color = models.CharField(max_length=100)
    hex = models.CharField(null=True, max_length=100)

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self):
        return f"{self.color}"


class Stock(models.Model):
    quantity = models.IntegerField()
    color = models.ForeignKey(to=Color, on_delete=models.CASCADE)
    size = models.ForeignKey(to=Size, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

    def __str__(self):
        return f"{self.quantity, self.color.color, self.size.size}"


class ProductGallery(models.Model):
    image = models.ImageField(upload_to="shop/products/gallery", null=True)

    def __str__(self):
        return f"{self.image.name}"

    class Meta:
        verbose_name = "Product Gallery"
        verbose_name_plural = "Products Gallery"


class Product(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    created_at = models.DateTimeField(default=now)
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, unique=True)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=10000)
    price = models.FloatField()
    quantity = models.ManyToManyField(to=Stock)
    thumbnail = models.ImageField(upload_to="shop/products/thumbnails")
    gallery = models.ManyToManyField(to=ProductGallery)
    rate = models.IntegerField()
    tags = models.ManyToManyField(to=ProductTags)
    full_description = models.TextField(max_length=100000)
    sku = models.IntegerField(default=0, unique=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    sales_counter = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(Product, self).save(*args, **kwargs)
