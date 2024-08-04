from django.shortcuts import render


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


def account_settings(request):
    return render(
        request=request,
        template_name="accounts/account-settings.html",
        context={
            "title": "Account Settings",
        }
    )
