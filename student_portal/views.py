from django.shortcuts import render, redirect
from .models import Announcement, MeetingMinute, Consul, Praetor, Quaestor, Aedile
from django.contrib.auth.decorators import login_required, permission_required
import datetime
from django.contrib.auth import logout
from django.contrib.auth.models import User
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
  consuls = Consul.objects.all()
  praetors = Praetor.objects.all()
  quaestors = Quaestor.objects.all()
  aediles = Aedile.objects.all() 
  return render(request, "student_portal/cursus.html", {"consuls": consuls, "praetors": praetors, "quaestors": quaestors, "aediles": aediles})

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
      return redirect("/student_portal/")
  return render(request, "student_portal/create_announce.html")

@permission_required("student_portal.add_meeting minute")
def create_minute(request):
  if request.method == "POST":
    contents = request.POST["contents"]
    if contents:
      date = datetime.datetime.now().strftime("%Y-%m-%d")
      new_minute = MeetingMinute(date=date, contents=contents)
      new_minute.save()
      return redirect("/student_portal/meeting-minutes")
  return render(request, "student_portal/create_minute.html")

def logout_request(request):
  logout(request)
  return redirect("index")

@permission_required("student_portal.edit_cursus")
def change_role(request):
  if request.method == "POST":
    student = request.POST["student"]
    position = request.POST["position"]
    if student and position:
      if position == "consul":
        user = User.objects.get(username=student)
        new_consul = Consul(user=user)
        new_consul.save()
      elif position == "praetor":
        user = User.objects.get(username=student)
        new_praetor = Praetor(user=user)
        new_praetor.save()
      elif position == "quaestor":
        user = User.objects.get(username=student)
        new_quaestor = Quaestor(user=user)
        new_quaestor.save()
      else:
        user = User.objects.get(username=student)
        new_aedile = Aedile(user=user)
        new_aedile.save()
      return redirect("/student_portal/cursus-honorum")        
  users = User.objects.all()
  return render(request, "student_portal/change_role.html", {"users": users})
