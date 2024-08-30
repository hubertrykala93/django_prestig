from django.db import models
from uuid import uuid4
from django.utils.timezone import now
from django.utils.text import slugify
from accounts.mixins import SaveMixin
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_save


class BrandLogo(SaveMixin, models.Model):
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="shop/brands")
    size = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    format = models.CharField(null=True)

    class Meta:
        verbose_name = "Brand Logo"
        verbose_name_plural = "Brand Logos"

    def __str__(self):
        return str(self.id)


class Brand(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    description = models.TextField(max_length=10000)
    logo = models.OneToOneField(to=BrandLogo, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Brand, self).save(*args, **kwargs)


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

        super(ProductTags, self).save(*args, **kwargs)


class ProductCategoryImage(SaveMixin, models.Model):
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="shop/categories")
    size = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    format = models.CharField(null=True)

    class Meta:
        verbose_name = "Product Category Image"
        verbose_name_plural = "Product Category Images"

    def __str__(self):
        return str(self.id)


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    category_image = models.OneToOneField(to=ProductCategoryImage, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(ProductCategory, self).save(*args, **kwargs)


class ProductSubCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField(upload_to='shop/subcategories')
    categories = models.ManyToManyField(to=ProductCategory, related_name="subcategories")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Product SubCategory"
        verbose_name_plural = "Product SubCategories"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(ProductSubCategory, self).save(*args, **kwargs)


class Size(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    def __str__(self):
        return f"{self.name}"


class Color(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    hex = models.CharField(null=True, max_length=100, unique=True)

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self):
        return f"{self.name}"


class Stock(models.Model):
    quantity = models.IntegerField()
    color = models.ForeignKey(to=Color, on_delete=models.CASCADE)
    size = models.ForeignKey(to=Size, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

    def __str__(self):
        return f"{self.quantity, self.color.name, self.size.name}"


class ProductGallery(models.Model):
    image = models.ImageField(upload_to="shop/products/gallery", null=True)

    class Meta:
        verbose_name = "Product Gallery"
        verbose_name_plural = "Products Gallery"

    def __str__(self):
        return f"{self.image.name}"


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
    image = models.ImageField(upload_to="shop/products/thumbnails")
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

        super(Product, self).save(*args, **kwargs)


@receiver(signal=post_save, sender=Brand)
def create_brand_logo(sender, instance=None, created=None, **kwargs):
    if created and not instance.logo:
        logo = BrandLogo.objects.create()
        instance.logo = logo
        instance.save()


@receiver(signal=post_delete, sender=Brand)
def delete_brand_logo(sender, instance, **kwargs):
    if instance.logo:
        instance.logo.delete()


@receiver(signal=post_save, sender=ProductCategory)
def created_product_category_image(sender, instance=None, created=None, **kwargs):
    if created and not instance.category_image:
        category_image = ProductCategoryImage.objects.create()
        instance.category_image = category_image
        instance.save()


@receiver(signal=post_delete, sender=ProductCategory)
def delete_product_category_image(sender, instance, **kwargs):
    if instance.category_image:
        instance.category_image.delete()
