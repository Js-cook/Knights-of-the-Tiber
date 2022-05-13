from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("constitution/", views.constitution, name="constitution")
]
