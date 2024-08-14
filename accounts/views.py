from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from accounts.models import Profile
from shop.api.serializers import DeliveryDetailsSerializer
from .api.serializers import UserSerializer, ProfileSerializer
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
            "user": UserSerializer(instance=request.user).data,
            "profile": ProfileSerializer(instance=request.user.profile).data,
            "delivery_details": DeliveryDetailsSerializer(instance=request.user.profile.delivery_details).data,
        }
    )


@login_required(login_url="login")
def account_settings(request):
    return render(
        request=request,
        template_name="accounts/account-settings.html",
        context={
            "title": "Account Settings",
            "account": UserSerializer(instance=request.user).data,
        }
    )


@login_required(login_url="login")
def profile_settings(request):
    profile = ProfileSerializer(instance=request.user.profile).data
    profile["profilepicture_name"] = profile["profilepicture"].split("/")[-1]

    return render(
        request=request,
        template_name="accounts/profile-settings.html",
        context={
            "title": "Profile Settings",
            "max": date.today().strftime("%Y-%m-%d"),
            "profile": profile,
            "genders": [choice[0] for choice in Profile._meta.get_field("gender").choices],
        }
    )


@login_required(login_url="login")
def delivery_details(request):
    return render(
        request=request,
        template_name="accounts/delivery-details.html",
        context={
            "title": "Delivery Details",
            "delivery_details": DeliveryDetailsSerializer(instance=request.user.profile.delivery_details).data,
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
