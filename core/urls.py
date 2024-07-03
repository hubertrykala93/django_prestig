from django.contrib import admin
from django.urls import path
from . import views as core_views

urlpatterns = [
    path(route='', view=core_views.index, name='index'),
    path(route='shop', view=core_views.shop, name="shop"),
    path(route="product", view=core_views.product, name="product"),
    path(route="blog", view=core_views.blog, name="blog"),
    path(route="contact-us", view=core_views.contact_us, name="contact-us"),
]
