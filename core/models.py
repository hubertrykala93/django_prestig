from django.db import models
from django.utils.timezone import now


class Newsletter(models.Model):
    created_at = models.DateTimeField(default=now)
    email = models.EmailField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"

    def __str__(self):
        return f"{self.email}"
