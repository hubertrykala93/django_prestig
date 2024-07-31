from django.shortcuts import render
from django.http import JsonResponse
import requests


def register(request):
    return render(
        request=request,
        template_name="accounts/register.html",
        context={
            "title": "Register",
            "img": "",
        }
    )


def login(request):
    return render(
        request=request,
        template_name="accounts/login.html",
        context={
            "title": "Login",
            "img": "",
        }
    )


def create_account(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("repassword")
        privacy_policy = request.POST.get("policy", False)

        response = requests.post(url="http://127.0.0.1:8000/api/v1/accounts/account-register", json={
            "username": username,
            "email": email,
            "password": password,
            "repassword": confirm_password,
            "policy": privacy_policy,
        })

        if response.status_code == 201:
            return JsonResponse(data=response.json())

        else:
            return JsonResponse(data=response.json())
