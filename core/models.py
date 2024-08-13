from django.db import models
from django.utils.timezone import now


class Newsletter(models.Model):
    created_at = models.DateTimeField(default=now)
    email = models.EmailField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"

    def __str__(self):
        return f"{self.email}"


class ContactMail(models.Model):
    date_sent = models.DateTimeField(default=now)
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    class Meta:
        verbose_name = "Contact Mail"
        verbose_name_plural = "Contact Mails"

    def __str__(self):
        return f"{self.fullname} | {self.email} | {self.subject}"
