from django.db import models
from django.utils.timezone import now
from accounts.models import User
from django.utils.text import slugify
from django.shortcuts import reverse
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
from PIL import Image


class ArticleCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Article Category"
        verbose_name_plural = "Article Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(viewname="articles-by-category", kwargs={
            "category_slug": self.slug,
        })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(ArticleCategory, self).save(*args, **kwargs)


class ArticleTag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Article Tag"
        verbose_name_plural = "Article Tags"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(viewname="articles-by-tag", kwargs={
            "tag_slug": self.slug,
        })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(ArticleTag, self).save(*args, **kwargs)


class ArticleImage(models.Model):
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="blog/article_images", null=True)
    size = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    format = models.CharField(max_length=100, null=True)
    alt = models.CharField(max_length=1000, null=True)

    class Meta:
        verbose_name = "Article Image"
        verbose_name_plural = "Article Images"

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super(ArticleImage, self).save(*args, **kwargs)

        if self.pk:
            self._resize_image()
            self._save_attributes()

            super(ArticleImage, self).save(*args, **kwargs)

        else:
            self._resize_image()
            self._save_attributes()

            super(ArticleImage, self).save(*args, **kwargs)

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


class Article(models.Model):
    created_at = models.DateTimeField(default=now)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    article_image = models.OneToOneField(to=ArticleImage, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=500, unique=True)
    description = models.TextField(max_length=100000)
    article_category = models.ForeignKey(to=ArticleCategory, on_delete=models.SET_NULL, null=True)
    article_tags = models.ManyToManyField(to=ArticleTag)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname="article-details", kwargs={
            "category_slug": self.article_category.slug,
            "article_slug": self.slug,
        })

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)

        if self.pk:
            article_image, created = ArticleImage.objects.get_or_create(article=self)

            self.article_image = article_image

        if not self.slug:
            self.slug = slugify(self.title)

        super(Article, self).save(*args, **kwargs)


class ArticleComment(models.Model):
    created_at = models.DateTimeField(default=now)
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    comment = models.TextField(max_length=20000)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.created_at}, {self.fullname if self.fullname else self.user.username}"

    def save(self, *args, **kwargs):
        if not self.email:
            self.email = self.user.email

        return super(ArticleComment, self).save(*args, **kwargs)


@receiver(signal=pre_delete, sender=Article)
def delete_article_image(sender, instance, **kwargs):
    if hasattr(instance, "article_image"):
        if instance.article_image and instance.article_image.image:
            image_path = instance.article_image.image.path

            if os.path.isfile(path=image_path):
                os.remove(path=image_path)

        instance.article_image.delete()
