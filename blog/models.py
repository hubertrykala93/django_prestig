from django.db import models
from django.utils.timezone import now
from accounts.models import User
from django.utils.text import slugify


class ArticleCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Article Category"
        verbose_name_plural = "Article Categories"

    def __str__(self):
        return self.name

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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super(ArticleTag, self).save(*args, **kwargs)


class Article(models.Model):
    created_at = models.DateTimeField(default=now)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500, unique=True)
    description = models.TextField(max_length=100000)
    article_category = models.ForeignKey(to=ArticleCategory, on_delete=models.SET_NULL, null=True)
    article_tag = models.ManyToManyField(to=ArticleTag)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super(Article, self).save(*args, **kwargs)


class ArticleComment(models.Model):
    created_at = models.DateTimeField(default=now)
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    message = models.TextField(max_length=20000)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.created_at}, {self.fullname if self.fullname else self.user.username}"
