from django.shortcuts import render, redirect
from .models import Announcement, MeetingMinute
from django.contrib.auth.decorators import login_required, permission_required
import datetime
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

# name
@permission_required("student_portal.add_announcement")
def create_announcement(request):
  if request.method == "POST":
    title = request.POST["title"]
    contents = request.POST["contents"]
    if title and contents:
      sender = request.user
      date = datetime.datetime.now().strftime("%Y-%m-%d")
      new_announcement = Announcement(title=title, contents=contents, sender=sender, date=date)
      new_announcement.save()
      return redirect("/student_portal/dashboard/")
  return render(request, "student_portal/create_announce.html")