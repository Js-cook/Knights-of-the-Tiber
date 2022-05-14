from django.shortcuts import render

# Create your views here.
def dashboard(request):
  return render(request, "student_portal/dashboard.html")

def announcements(request):
  return render(request, "student_portal/announcements.html")

def minutes(request):
  return render(request, "student_portal/minutes.html")

def cursus(request):
  return render(request, "student_portal/cursus.html")