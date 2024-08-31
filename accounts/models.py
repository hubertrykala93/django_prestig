from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils.timezone import now
from uuid import uuid4
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_delete, pre_save, post_migrate, post_init, pre_init, \
    pre_migrate
from shop.models import Product
from .mixins import SaveMixin
import os


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
    uuid = models.UUIDField(default=uuid4, unique=True)
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
    uuid = models.UUIDField(default=uuid4, unique=True)

    class Meta:
        verbose_name = "One Time Password"
        verbose_name_plural = "One Time Passwords"

    def __str__(self):
        return self.user.username


class DeliveryDetails(models.Model):
    created_at = models.DateTimeField(default=now)
    uuid = models.UUIDField(default=uuid4, unique=True)
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
        return f"{self.id}"


class ProfilePicture(SaveMixin, models.Model):
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default="accounts/profile_images/default_profile_image.png",
                              upload_to="accounts/profile_images", null=True)
    size = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    format = models.CharField(null=True)

    class Meta:
        verbose_name = "Profile Picture"
        verbose_name_plural = "Profile Pictures"

    def __str__(self):
        return f"{self.id}"


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
    profilepicture = models.OneToOneField(to=ProfilePicture, on_delete=models.CASCADE, null=True)

    # Social Media
    facebook = models.CharField(max_length=50, null=True)
    instagram = models.CharField(max_length=50, null=True)

    # Order Information
    wishlist = models.ManyToManyField(to=Product)

    # Delivery Details
    delivery_details = models.OneToOneField(to=DeliveryDetails, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance=None, created=None, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


@receiver(signal=post_save, sender=Profile)
def create_delivery_details(sender, instance=None, created=None, **kwargs):
    if created and not instance.delivery_details:
        delivery_details = DeliveryDetails.objects.create()
        instance.delivery_details = delivery_details
        instance.save()


@receiver(signal=post_save, sender=Profile)
def create_profilepicture(sender, instance=None, created=None, **kwargs):
    if created and not instance.profilepicture:
        profilepicture = ProfilePicture.objects.create()
        instance.profilepicture = profilepicture
        instance.save()


@receiver(signal=post_delete, sender=Profile)
def delete_delivery_details(sender, instance, **kwargs):
    if instance.delivery_details:
        instance.delivery_details.delete()


@receiver(signal=post_delete, sender=Profile)
def delete_profilepicture(sender, instance, **kwargs):
    if instance.profilepicture:
        instance.profilepicture.delete()


@receiver(signal=pre_delete, sender=Profile)
def delete_profilepicture_file_when_profile_is_deleting(sender, instance, **kwargs):
    if instance.profilepicture and instance.profilepicture.image:
        image_path = instance.profilepicture.image.path

        if 'default_profile_image.png' not in image_path:
            if os.path.isfile(path=image_path):
                os.remove(path=image_path)


@receiver(signal=pre_delete, sender=User)
def delete_profilepicture_file_when_user_is_deleting(sender, instance, **kwargs):
    if instance.profile.profilepicture and instance.profile.profilepicture.image:
        image_path = instance.profile.profilepicture.image.path

        if 'default_profile_image.png' not in image_path:
            if os.path.isfile(path=image_path):
                os.remove(path=image_path)
