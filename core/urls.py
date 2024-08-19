from django.urls import path
from . import views as core_views

urlpatterns = [
    path(route="", view=core_views.index, name="index"),
    path(route="about", view=core_views.about, name="about"),
    path(route="product", view=core_views.product, name="product"),
    path(route="contact-us", view=core_views.contact_us, name="contact-us"),
    path(route="privacy-policy", view=core_views.privacy_policy, name="privacy-policy"),
    path(route="error-404", view=core_views.error404, name="error-404"),
]
