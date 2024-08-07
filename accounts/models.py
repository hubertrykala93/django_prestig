from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils.timezone import now
from uuid import uuid4
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image


class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address.")

        email = self.normalize_email(email=email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(raw_password=password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(
            username=username, email=email, password=password, **extra_fields
        )

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(
            username=username, email=email, password=password, **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid4)
    date_joined = models.DateTimeField(default=now)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return f"{self.username}"


class Profile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    short_description = models.CharField(max_length=500)
    gender = models.CharField(
        choices=(
            ("Male", "Male"),
            ("Female", "Female"),
            ("Undefined", "Undefined"),
        )
    )
    date_of_birth = models.DateTimeField(null=True)
    image = models.ImageField(default="profile_images/default_profile_image.png", upload_to="profile_images",
                              null=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address_line = models.CharField(max_length=200)  # including street, house number, apartment number
    postal_code = models.CharField(max_length=100)
    website = models.URLField(null=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        image = Image.open(fp=self.image.path)

        if image.mode == "RGBA":
            image.convert(mode="RGB")

        if image.width > 300 or image.height > 300:
            image.thumbnail(size=(300, 300))
            image.save(fp=self.image.path)

        return super(Profile, self).save(*args, **kwargs)


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance=None, created=None, **kwargs):
    if created:
        Profile.objects.create(user=instance)
