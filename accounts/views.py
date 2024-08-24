from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from accounts.models import Profile, OneTimePassword, User, DeliveryDetails
from datetime import date
from django.core.exceptions import ValidationError
import requests


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


def profile_page(request):
    return render(
        request=request,
        template_name="accounts/profile-page.html",
    )


@login_required(login_url="login")
def my_account(request):
    return render(
        request=request,
        template_name="accounts/my-account.html",
        context={
            "title": "My Account",
            "user": request.user,
            "profile": request.user.profile,
            "delivery_details": request.user.profile.delivery_details,
        }
    )


@login_required(login_url="login")
def account_settings(request):
    return render(
        request=request,
        template_name="accounts/account-settings.html",
        context={
            "title": "Account Settings",
            "account": request.user,
        }
    )


@login_required(login_url="login")
def profile_settings(request):
    return render(
        request=request,
        template_name="accounts/profile-settings.html",
        context={
            "title": "Profile Settings",
            "max": date.today().strftime("%Y-%m-%d"),
            "profile": request.user.profile,
            "genders": [choice[0] for choice in Profile._meta.get_field("gender").choices],
        }
    )


def comments_summary(request):
    return render(
        request=request,
        template_name="accounts/comments-summary.html",
        context={
            "title": "Comments Summary",
        }
    )


@login_required(login_url="login")
def delivery_details(request):
    return render(
        request=request,
        template_name="accounts/delivery-details.html",
        context={
            "title": "Delivery Details",
            "delivery_details": request.user.profile.delivery_details,
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


@user_passes_test(test_func=lambda u: not u.is_authenticated, login_url="index")
def forgot_password(request):
    return render(
        request=request,
        template_name="accounts/forgot-password.html",
        context={
            "title": "Forgot Password",
        },
    )


@user_passes_test(test_func=lambda u: not u.is_authenticated, login_url="index")
def change_password(request):
    token = request.GET.get("token")

    try:
        one_time_password = OneTimePassword.objects.get(uuid=token)

    except ValidationError:
        return redirect(to="error-404")

    return render(
        request=request,
        template_name="accounts/change-password.html",
        context={
            "title": "Change Password",
            "token": token,
        },
    )
