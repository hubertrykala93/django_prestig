from django.db import models
from django.utils.timezone import now
from accounts.models import User
from django.utils.text import slugify
from uuid import uuid4
from PIL import Image
import os
from django.conf import settings
from django.shortcuts import reverse


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


class Article(models.Model):
    created_at = models.DateTimeField(default=now)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="article_images", null=True)
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

        image = Image.open(fp=self.image.path)

        if image.mode == "RGBA":
            image = image.convert(mode="RGB")

        img_width = image.width
        img_height = image.height

        output_width = 1100
        output_height = img_height * output_width / img_width

        image.thumbnail(size=(output_width, output_height))

        file_extension = self.image.name.split(".")[-1]
        new_name = str(uuid4()) + "." + file_extension
        new_path = os.path.join(os.path.dirname(self.image.path), new_name)

        image.save(fp=new_path)
        self.image.name = os.path.relpath(new_path, start=settings.MEDIA_ROOT)

        if not self.slug:
            self.slug = slugify(self.title)

        return super(Article, self).save(*args, **kwargs)


class ArticleComment(models.Model):
    created_at = models.DateTimeField(default=now)
    article = models.ForeignKey(to=Article, related_name="comments", on_delete=models.CASCADE)
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
