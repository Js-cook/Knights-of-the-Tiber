from django.shortcuts import render
from .models import Announcement, MeetingMinute
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
  announcements = Announcement.objects.all()
  return render(request, "student_portal/dashboard.html", {"announcements": announcements})
  
@login_required
def minutes(request):
  minutes = MeetingMinute.objects.all()
  return render(request, "student_portal/minutes.html", {"minutes": minutes})

@login_required
def cursus(request):
  return render(request, "student_portal/cursus.html")