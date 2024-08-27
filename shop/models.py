from django.db import models
from uuid import uuid4
from django.utils.timezone import now
from django.utils.text import slugify
import os
from PIL import Image
from django.conf import settings


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
        if not getattr(self, "_is_saving", False):
            self._is_saving = True

            if self.logo:
                if Brand.objects.filter(pk=self.pk).exists():
                    instance = Brand.objects.get(pk=self.pk)

                    try:
                        os.remove(path=instance.logo.path)

                    except FileNotFoundError:
                        super(Brand, self).save(*args, **kwargs)

                super(Brand, self).save(*args, **kwargs)

                original_path = self.logo.path

                image = Image.open(fp=original_path)
                image.thumbnail(size=(300, 300))

                file_extension = original_path.split(".")[-1]
                new_name = str(uuid4()) + "." + file_extension
                new_path = os.path.join(os.path.dirname(original_path), new_name)

                os.remove(path=original_path)

                image.save(fp=new_path)

                self.image.name = os.path.relpath(path=new_path, start=settings.MEDIA_ROOT)

                if not self.slug:
                    self.slug = slugify(self.name)

                super(Brand, self).save(update_fields=["slug", "image"])

            else:
                super(Brand, self).save(*args, **kwargs)

            self._is_saving = True

        else:
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

        return super(ProductTags, self).save(*args, **kwargs)


class ProductSubCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='shop/subcategories')

    class Meta:
        verbose_name = "Product SubCategory"
        verbose_name_plural = "Product SubCategories"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not getattr(self, "is_saving", False):
            self._is_saving = True

            if self.image:
                if ProductSubCategory.objects.filter(pk=self.pk).exists():
                    instance = ProductSubCategory.objects.get(pk=self.pk)

                    try:
                        os.remove(path=instance.image.path)

                    except FileNotFoundError:
                        super(ProductSubCategory, self).save(*args, **kwargs)

                super(ProductSubCategory, self).save(*args, **kwargs)

                original_path = self.image.path

                image = Image.open(fp=original_path)

                img_width = image.width
                img_height = image.height

                output_width = img_width
                output_height = img_height * output_width / img_width

                image.thumbnail(size=(output_width, output_height))

                file_extension = original_path.split(".")[-1]
                new_name = str(uuid4()) + "." + file_extension
                new_path = os.path.join(os.path.dirname(original_path), new_name)

                os.remove(path=original_path)

                image.save(fp=new_path)

                self.image.name = os.path.relpath(path=new_path, start=settings.MEDIA_ROOT)

                if not self.slug:
                    self.slug = slugify(self.name)

                super(ProductSubCategory, self).save(update_fields=["image", "slug"])

            else:
                super(ProductSubCategory, self).save(*args, **kwargs)

            self._is_saving = True

        else:
            super(ProductSubCategory, self).save(*args, **kwargs)


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
        if not getattr(self, "_is_saving", False):
            self._is_saving = True

            if self.image:
                if ProductCategory.objects.filter(pk=self.pk).exists():
                    instance = ProductCategory.objects.get(pk=self.pk)

                    try:
                        os.remove(path=instance.image.path)

                    except FileNotFoundError:
                        super(ProductCategory, self).save(*args, **kwargs)

                super(ProductCategory, self).save(*args, **kwargs)

                original_path = self.image.path

                image = Image.open(fp=original_path)

                img_width = image.width
                img_height = image.height

                output_width = 1100
                output_height = img_height * output_width / img_width

                image.thumbnail(size=(output_width, output_height))

                file_extension = original_path.split(".")[-1]
                new_name = str(uuid4()) + "." + file_extension
                new_path = os.path.join(os.path.dirname(p=original_path), new_name)

                os.remove(path=original_path)

                image.save(fp=new_path)

                self.image.name = os.path.relpath(path=new_path, start=settings.MEDIA_ROOT)

                if not self.slug:
                    self.slug = slugify(self.name)

                super(ProductCategory, self).save(update_fields=["image", "slug"])

            else:
                super(ProductCategory, self).save(*args, **kwargs)

            self._is_saving = True

        else:
            super(ProductCategory, self).save(*args, **kwargs)


class Size(models.Model):
    size = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    def __str__(self):
        return f"{self.size}"


class Color(models.Model):
    color = models.CharField(max_length=100, unique=True)
    hex = models.CharField(null=True, max_length=100, unique=True)

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

    def save(self, *args, **kwargs):
        if not getattr(self, "_is_saving", False):
            self._is_saving = True

            if self.image:
                if ProductGallery.objects.filter(pk=self.pk).exists():
                    instance = ProductGallery.objects.get(pk=self.pk)

                    try:
                        os.remove(path=instance.image.path)

                    except FileNotFoundError:
                        super(ProductGallery, self).save(*args, **kwargs)

                super(ProductGallery, self).save(*args, **kwargs)

                original_path = self.image.path

                image = Image.open(fp=original_path)

                img_width = image.width
                img_height = image.height

                output_width = 1100
                output_height = img_height * output_width / img_width

                image.thumbnail(size=(output_width, output_height))

                file_extension = original_path.split(".")[-1]
                new_name = str(uuid4()) + "." + file_extension
                new_path = os.path.join(os.path.dirname(p=original_path), new_name)

                os.remove(path=original_path)

                image.save(fp=new_path)

                self.image.name = os.path.relpath(path=new_path, start=settings.MEDIA_ROOT)

                super(ProductGallery, self).save(*args, **kwargs)

            else:
                super(ProductGallery, self).save(*args, **kwargs)

            self._is_saving = True

        else:
            super(ProductGallery, self).save(*args, **kwargs)


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
        if not getattr(self, "_is_saving", False):
            self._is_saving = True

            if self.thumbnail:
                if Product.objects.filter(pk=self.pk).exists():
                    instance = Product.objects.get(pk=self.pk)

                    try:
                        os.remove(path=instance.thumbnail.path)

                    except FileNotFoundError:
                        super(Product, self).save(*args, **kwargs)

                super(Product, self).save(*args, **kwargs)

                original_path = self.thumbnail.path

                image = Image.open(fp=original_path)

                img_width = image.width
                img_height = image.height

                output_width = 1100
                output_height = img_height * output_width / img_width

                image.thumbnail(size=(output_width, output_height))

                file_extension = original_path.split(".")[-1]
                new_name = str(uuid4()) + "." + file_extension
                new_path = os.path.join(os.path.dirname(p=original_path), new_name)

                os.remove(path=original_path)

                image.save(fp=new_path)

                self.image.name = os.path.relpath(path=new_path, start=settings.MEDIA_ROOT)

                if not self.slug:
                    self.slug = slugify(self.name)

                super(Product, self).save(update_fields=["image", "slug"])

            else:
                super(Product, self).save(*args, **kwargs)

            self._is_saving = True

        else:
            super(Product, self).save(*args, **kwargs)
