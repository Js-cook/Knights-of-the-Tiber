from django.urls import path
from . import views

app_name = "student_portal"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    # path("announcements", views.announcements, name="announcements"),
    path("cursus-honorum", views.cursus, name="cursus_honorum"),
    path("meeting-minutes", views.minutes, name="minutes")
]
