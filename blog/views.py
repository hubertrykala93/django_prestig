from django.shortcuts import render


def blog(request):
    return render(
        request=request,
        template_name="core/blog.html",
        context={
            "title": "Blog",
        }
    )
