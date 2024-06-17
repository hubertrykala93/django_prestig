from django.contrib import admin
from django.urls import path
from . import views as core_views

urlpatterns = [
    path(route='', view=core_views.index, name='index'),
    path(route='send-file', view=core_views.send_file, name='send-file'),
]
