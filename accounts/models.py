from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils.timezone import now
from uuid import uuid4
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from shop.models import Product
import os
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

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        if self.pk:
            profile, created = Profile.objects.get_or_create(user=self)

            if created:
                profile_picture = ProfilePicture.objects.create()
                profile.profilepicture = profile_picture

                delivery_details = DeliveryDetails.objects.create()
                profile.delivery_details = delivery_details

                profile.save()


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


class ProfilePicture(models.Model):
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default="accounts/profile_images/default_profile_image.png",
                              upload_to="accounts/profile_images", null=True)
    size = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    format = models.CharField(max_length=100, null=True)
    alt = models.CharField(max_length=1000, null=True)

    class Meta:
        verbose_name = "Profile Picture"
        verbose_name_plural = "Profile Pictures"

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        if self.id:
            super(ProfilePicture, self).save(*args, **kwargs)

            instance = ProfilePicture.objects.get(id=self.id)

            self._resize_image()
            self._save_attributes(instance=instance)

            super(ProfilePicture, self).save(*args, **kwargs)

        else:
            self._resize_image()
            self._save_attributes()

            super(ProfilePicture, self).save(*args, **kwargs)

    def _resize_image(self):
        image = Image.open(fp=self.image.path)

        if image.mode == "RGBA":
            image = image.convert(mode="RGB")

        image.thumbnail(size=(300, 300))
        image.save(fp=self.image.path)

        return image

    def _save_attributes(self, instance=None):
        image = self._resize_image()

        if "default_profile_image.png" in self.image.path:
            self.alt = "Default profile picture"

        if instance:
            profile = Profile.objects.get(profilepicture_id=instance.id)
            user = Profile.objects.get(profilepicture_id=instance.id).user

            if profile.firstname and profile.lastname:
                self.alt = f"{profile.firstname.capitalize()} {profile.lastname.capitalize()} profile picture"

            else:
                self.alt = f"{user.username} profile picture"

        self.size = os.path.getsize(filename=self.image.path)
        self.width, self.height = image.width, image.height
        self.format = image.format


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
        default="Undefined",
        max_length=100
    )
    dateofbirth = models.DateField(null=True)
    profilepicture = models.OneToOneField(to=ProfilePicture, on_delete=models.SET_NULL, null=True)

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


@receiver(signal=pre_delete, sender=User)
def delete_profile(sender, instance, **kwargs):
    try:
        profile = instance.profile

    except Profile.DoesNotExist:
        return

    if instance.profile:
        profile = instance.profile

        if hasattr(profile, "profilepicture"):
            if profile.profilepicture and profile.profilepicture.image:
                image_path = profile.profilepicture.image.path

                if "default_profile_image.png" not in image_path:
                    if os.path.isfile(path=image_path):
                        os.remove(path=image_path)

            profile.profilepicture.delete()

    if instance.profile.delivery_details:
        instance.profile.delivery_details.delete()

    if instance.profile:
        instance.profile.delete()
