import os
from PIL import Image
from django.db import models
from uuid import uuid4
from django.utils.timezone import now
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.shortcuts import reverse
from django.db.models import Avg


class BrandLogo(models.Model):
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="shop/brands")
    size = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    format = models.CharField(max_length=100, null=True)
    alt = models.CharField(max_length=1000, null=True)

    class Meta:
        verbose_name = "Brand Logo"
        verbose_name_plural = "Brand Logos"

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super(BrandLogo, self).save(*args, **kwargs)

        if self.pk:
            self._resize_image()
            self._save_attributes()

            super(BrandLogo, self).save(*args, **kwargs)

        else:
            self._resize_image()
            self._save_attributes()

            super(BrandLogo, self).save(*args, **kwargs)

    def _resize_image(self):
        image = Image.open(fp=self.image.path)

        if image.mode == "RGBA":
            image = image.convert(mode="RGB")

        image.thumbnail(size=(300, 300))
        image.save(fp=self.image.path)

        return image

    def _save_attributes(self):
        image = self._resize_image()

        self.size = os.path.getsize(filename=self.image.path)
        self.width, self.height = image.width, image.height
        self.format = image.format


class Brand(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    description = models.TextField(max_length=10000)
    logo = models.OneToOneField(to=BrandLogo, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        super(Brand, self).save(*args, **kwargs)

        if self.pk:
            logo, created = BrandLogo.objects.get_or_create(brand=self)

            self.logo = logo

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


class ProductCategoryImage(models.Model):
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="shop/categories")
    size = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    format = models.CharField(max_length=100, null=True)
    alt = models.CharField(max_length=1000, null=True)

    class Meta:
        verbose_name = "Product Category Image"
        verbose_name_plural = "Product Category Images"

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super(ProductCategoryImage, self).save(*args, **kwargs)

        if self.pk:
            self._resize_image()
            self._save_attributes()

            super(ProductCategoryImage, self).save(*args, **kwargs)

        else:
            self._resize_image()
            self._save_attributes()

            super(ProductCategoryImage, self).save(*args, **kwargs)

    def _resize_image(self):
        image = Image.open(fp=self.image.path)

        if image.mode == "RGBA":
            image = image.convert(mode="RGB")

        if image.width > image.height:
            output_size = (1100, image.height * 1100 / image.width)

        else:
            output_size = (1100 * image.width / image.height, 1100)

        image.thumbnail(size=output_size)
        image.save(fp=self.image.path)

        return image

    def _save_attributes(self):
        image = self._resize_image()

        self.size = os.path.getsize(filename=self.image.path)
        self.width, self.height = image.width, image.height
        self.format = image.format


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    category_image = models.OneToOneField(to=ProductCategoryImage, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        super(ProductCategory, self).save(*args, **kwargs)

        if self.pk:
            category_image, created = ProductCategoryImage.objects.get_or_create(productcategory=self)

            self.category_image = category_image

        if not self.slug:
            self.slug = slugify(self.name)

        super(ProductCategory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            viewname="products-by-category",
            kwargs={
                "category_slug": self.slug,
            }
        )


class ProductSubCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE, null=True,
                                 related_name="subcategories")
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


class ProductImage(models.Model):
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="shop/products")
    size = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    format = models.CharField(max_length=100, null=True)
    alt = models.CharField(max_length=1000, null=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super(ProductImage, self).save(*args, **kwargs)

        if self.pk:
            self._resize_image()
            self._save_attributes()

            super(ProductImage, self).save(*args, **kwargs)

        else:
            self._resize_image()
            self._save_attributes()

            super(ProductImage, self).save(*args, **kwargs)

    def _resize_image(self):
        image = Image.open(fp=self.image.path)

        if image.mode == "RGBA":
            image = image.convert(mode="RGB")

        output_size = (1100, image.height * 1100 / image.width)

        image.thumbnail(size=output_size)
        image.save(fp=self.image.path)

        return image

    def _save_attributes(self):
        image = self._resize_image()

        self.size = os.path.getsize(filename=self.image.path)
        self.width, self.height = image.width, image.height
        self.format = image.format


class Product(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    created_at = models.DateTimeField(default=now)
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(to=ProductSubCategory, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=1000, unique=True)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=10000)
    price = models.FloatField()
    gallery = models.ManyToManyField(to=ProductImage, blank=True)
    tags = models.ManyToManyField(to=ProductTags)
    full_description = models.TextField(max_length=100000)
    sku = models.CharField(max_length=100, unique=True)
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

        if not self.sku:
            self.sku = str(uuid4()).split("-")[-1]

        super(Product, self).save(*args, **kwargs)

    def get_featured_image(self):
        for image in self.gallery.all():
            if image.is_featured:
                return image

    def get_absolute_url(self):
        return reverse(
            viewname="product-details",
            kwargs={
                "category_slug": self.category.slug,
                "subcategory_slug": self.subcategory.slug,
                "product_slug": self.slug,
            }
        )

    def average_rating(self):
        return int(self.productreview_set.aggregate(Avg("rate"))["rate__avg"])


class Stock(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    color = models.ForeignKey(to=Color, on_delete=models.CASCADE)
    size = models.ForeignKey(to=Size, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"
        unique_together = ("product", "color", "size")

    def __str__(self):
        return f"{self.product.id, self.quantity, self.color.name, self.size.name}"


class ProductReview(models.Model):
    created_at = models.DateTimeField(default=now)
    user = models.ForeignKey(to="accounts.User", on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=1000)
    rate = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Product Review"
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return f"Review by {self.user} for {self.product}"


@receiver(signal=pre_delete, sender=Brand)
def delete_brand_logo(sender, instance, **kwargs):
    if hasattr(instance, "logo"):
        if instance.logo and instance.logo.image:
            image_path = instance.logo.image.path

            if os.path.isfile(path=image_path):
                os.remove(path=image_path)

        instance.logo.delete()


@receiver(signal=pre_delete, sender=ProductCategory)
def delete_product_category_image(sender, instance, **kwargs):
    if hasattr(instance, "category_image"):
        if instance.category_image and instance.category_image.image:
            image_path = instance.category_image.image.path

            if os.path.isfile(path=image_path):
                os.remove(path=image_path)

        instance.category_image.delete()


@receiver(signal=pre_delete, sender=Product)
def delete_product_images(sender, instance, **kwargs):
    if hasattr(instance, "gallery"):
        if instance.gallery:
            image_paths = [obj.image.path for obj in instance.gallery.all()]

            for img in image_paths:
                if os.path.isfile(path=img):
                    os.remove(path=img)

        if instance.gallery:
            for img in instance.gallery.all():
                img.delete()
