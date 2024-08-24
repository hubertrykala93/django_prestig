from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils.timezone import now
from uuid import uuid4
from django.dispatch import receiver
from django.db.models.signals import post_save
from shop.models import Product
from PIL import Image
import os
from django.conf import settings


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
    username = models.CharField(max_length=35, unique=True)
    email = models.EmailField(max_length=255, unique=True)
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


class OneTimePassword(models.Model):
    created_at = models.DateTimeField(default=now)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid4)

    class Meta:
        verbose_name = "One Time Password"
        verbose_name_plural = "One Time Passwords"

    def __str__(self):
        return self.user.username


class DeliveryDetails(models.Model):
    created_at = models.DateTimeField(default=now)
    uuid = models.UUIDField(default=uuid4)
    phone = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=56)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=169)
    street = models.CharField(max_length=50)
    housenumber = models.CharField(max_length=5)  # Include the house number if the delivery is to a residential home
    apartmentnumber = models.CharField(
        max_length=5)  # Include the apartment number if the delivery is to a building with multiple units
    postalcode = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Delivery Detail"
        verbose_name_plural = "Delivery Details"

    def __str__(self):
        return str(self.uuid)


class Profile(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Undefined", "Undefined"),
    )
    created_at = models.DateTimeField(default=now)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    # Basic Info
    firstname = models.CharField(max_length=35)
    lastname = models.CharField(max_length=35)
    bio = models.CharField(max_length=150)
    gender = models.CharField(
        choices=GENDER_CHOICES,
        default="Undefined")
    dateofbirth = models.DateField(null=True)
    profilepicture = models.ImageField(default="profile_images/default_profile_image.png", upload_to="profile_images/",
                                       null=True)

    # Social Media
    facebook = models.CharField(max_length=50, null=True)
    instagram = models.CharField(max_length=50, null=True)

    # Order Information
    wishlist = models.ManyToManyField(to=Product)

    # Delivery Details
    delivery_details = models.OneToOneField(to=DeliveryDetails, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # super(Profile, self).save(*args, **kwargs)

        if self.profilepicture:
            print("If profile picture.")
            super(Profile, self).save(*args, **kwargs)

            original_path = self.profilepicture.path
            print(f"Original path -> {original_path}")

            image = Image.open(fp=self.profilepicture.path)
            image.thumbnail(size=(300, 300))
            print(f"Picture lower.")

            file_extension = self.profilepicture.name.split(".")[-1]
            print(f"File Extension -> {file_extension}")
            new_name = str(uuid4()) + "." + file_extension
            print(f"New name -> {new_name}")
            new_path = os.path.join(os.path.dirname(self.profilepicture.path), new_name)
            print(f"New path -> {new_path}")

            image.save(fp=new_path)
            print(f"Image saved.")
            self.profilepicture.name = os.path.relpath(new_path, start=settings.MEDIA_ROOT)

            if original_path != new_path:
                print("Original Path != New Path")
                if os.path.exists(path=original_path):
                    print("Exist")
                    os.remove(path=original_path)

            super(Profile, self).save(*args, **kwargs)

        else:
            super(Profile, self).save(*args, **kwargs)


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance=None, created=None, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(signal=post_save, sender=Profile)
def create_delivery_details(sender, instance=None, created=None, **kwargs):
    if created:
        delivery_details = DeliveryDetails.objects.create()
        instance.delivery_details = delivery_details
        instance.save()
