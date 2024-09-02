import os
from PIL import Image
from django.db import models
from uuid import uuid4
from django.utils.timezone import now
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_delete


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

        output_size = (1100, image.height * 1100 / image.width)

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


class ProductSubCategoryImage(models.Model):
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="shop/subcategories")
    size = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    format = models.CharField(max_length=100, null=True)
    alt = models.CharField(max_length=1000, null=True)

    class Meta:
        verbose_name = "Product SubCategory Image"
        verbose_name_plural = "Product SubCategory Images"

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super(ProductSubCategoryImage, self).save(*args, **kwargs)

        if self.pk:
            self._resize_image()
            self._save_attributes()

            super(ProductSubCategoryImage, self).save(*args, **kwargs)

        else:
            self._resize_image()
            self._save_attributes()

            super(ProductSubCategoryImage, self).save(*args, **kwargs)

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


class ProductSubCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    subcategory_image = models.OneToOneField(to=ProductSubCategoryImage, on_delete=models.SET_NULL, null=True)
    categories = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE, null=True, related_name="category")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Product SubCategory"
        verbose_name_plural = "Product SubCategories"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        super(ProductSubCategory, self).save(*args, **kwargs)

        if self.pk:
            subcategory_image, created = ProductSubCategoryImage.objects.get_or_create(productsubcategory=self)

            self.subcategory_image = subcategory_image

        if not self.slug:
            self.slug = f"{self.categories.name.lower()}-{slugify(self.name)}"

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
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, unique=True)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=10000)
    price = models.FloatField()
    quantity = models.ManyToManyField(to=Stock)
    gallery = models.ManyToManyField(to=ProductImage, blank=True)
    rate = models.IntegerField(null=True)
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


@receiver(signal=pre_delete, sender=ProductSubCategory)
def delete_product_subcategory_image(sender, instance, **kwargs):
    if hasattr(instance, "subcategory_image"):
        if instance.subcategory_image and instance.subcategory_image.image:
            image_path = instance.subcategory_image.image.path

            if os.path.isfile(path=image_path):
                os.remove(path=image_path)

        instance.subcategory_image.delete()


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
