from django.shortcuts import render
from .models import Announcement, MeetingMinute
# Create your views here.
def dashboard(request):
  return render(request, "student_portal/dashboard.html")

# Prolly going to remove this page and add it to dashboard
def announcements(request):
  return render(request, "student_portal/announcements.html")

def minutes(request):
  minutes = MeetingMinute.objects.all()
  return render(request, "student_portal/minutes.html", {"minutes": minutes})

def cursus(request):
  return render(request, "student_portal/cursus.html")