from django.urls import path
from . import views as core_views

urlpatterns = [
    path(route='', view=core_views.index, name='index'),
    path(route='about', view=core_views.about, name='about'),
    path(route='shop', view=core_views.shop, name="shop"),
    path(route="product", view=core_views.product, name="product"),
    path(route="blog", view=core_views.blog, name="blog"),
    path(route="contact-us", view=core_views.contact_us, name="contact-us"),
    path(route="create-newsletter", view=core_views.create_newsletter, name="create-newsletter"),
    path(route="send-contact-mail", view=core_views.send_contact_mail, name="send-contact-mail"),
    path(route="privacy-policy", view=core_views.privacy_policy, name="privacy-policy"),
]
