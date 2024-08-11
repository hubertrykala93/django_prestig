from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from accounts.models import Profile, User
from shop.models import DeliveryDetails
from shop.api.serializers import DeliveryDetailsSerializer
from .api.serializers import UserSerializer, ProfileSerializer
import requests
from datetime import date


@user_passes_test(test_func=lambda u: not u.is_authenticated, login_url="index")
def register(request):
    return render(
        request=request,
        template_name="accounts/register.html",
        context={
            "title": "Register",
            "img": "",
        }
    )


@user_passes_test(test_func=lambda u: not u.is_authenticated, login_url="index")
def login(request):
    return render(
        request=request,
        template_name="accounts/login.html",
        context={
            "title": "Login",
            "img": "",
        }
    )


@login_required(login_url="login")
def my_account(request):
    return render(
        request=request,
        template_name="accounts/my-account.html",
        context={
            "title": "My Account",
        }
    )


@login_required(login_url="login")
def account_settings(request):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(instance=user)

    return render(
        request=request,
        template_name="accounts/account-settings.html",
        context={
            "title": "Account Settings",
            "account": serializer.data,
        }
    )


@login_required(login_url="login")
def profile_settings(request):
    profile = Profile.objects.get(user_id=request.user.id)
    serializer = ProfileSerializer(instance=profile)

    return render(
        request=request,
        template_name="accounts/profile-settings.html",
        context={
            "title": "Profile Settings",
            "max": date.today().strftime("%Y-%m-%d"),
            "profile": serializer.data,
            "genders": [choice[0] for choice in Profile._meta.get_field("gender").choices],
        }
    )


@login_required(login_url="login")
def delivery_details(request):
    delivery_details = DeliveryDetails.objects.get(id=Profile.objects.get(user_id=request.user.id).delivery_details_id)
    serializer = DeliveryDetailsSerializer(instance=delivery_details)

    return render(
        request=request,
        template_name="accounts/delivery-details.html",
        context={
            "title": "Delivery Details",
            "delivery_details": serializer.data,
        }
    )


@login_required(login_url="login")
def purchased_products(request):
    return render(
        request=request,
        template_name="accounts/purchased-products.html",
        context={
            "title": "Purchased Products",
        }
    )


@login_required(login_url="login")
def product_returns(request):
    return render(
        request=request,
        template_name="accounts/product-returns.html",
        context={
            "title": "Product Returns",
        }
    )


@login_required(login_url="login")
def product_reviews(request):
    return render(
        request=request,
        template_name="accounts/product-reviews.html",
        context={
            "title": "Product Reviews",
        }
    )
