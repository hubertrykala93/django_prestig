from django.shortcuts import render


def shop(request):
    return render(
        request=request,
        template_name="shop/shop.html",
        context={
            "title": "Shop",
        }
    )
