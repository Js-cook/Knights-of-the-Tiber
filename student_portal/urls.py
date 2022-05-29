from django.urls import path
from . import views

app_name = "student_portal"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    # path("announcements", views.announcements, name="announcements"),
    path("cursus-honorum", views.cursus, name="cursus_honorum"),
    path("meeting-minutes", views.minutes, name="minutes"),
    path("new-announcement", views.create_announcement, name="new_announcement"),
    path("new-meeting-minute", views.create_minute, name="new_minute"),
    path("change-role", views.change_role, name="change_role")
]
