from django.urls import path
from . import views as accounts_views

urlpatterns = [
    path(route="register", view=accounts_views.register, name="register"),
    path(route="login", view=accounts_views.login, name="login"),
    path(route="create-account", view=accounts_views.create_account, name="create-account"),
    path(route="authenticate", view=accounts_views.authenticate, name="authenticate"),
]
