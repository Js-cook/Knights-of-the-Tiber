from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("constitution/", views.constitution, name="constitution"),
    path("contact/", views.contact, name="contact"),
    path("news/", views.news, name="news"),
    path("club-news/", views.club_news, name="club-news")
]
