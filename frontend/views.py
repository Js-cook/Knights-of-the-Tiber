from django.shortcuts import render
from student_portal.models import Consul, Praetor, Quaestor, Aedile

# Create your views here.
def index(request):
  return render(request, "frontend/index.html")

def constitution(request):
  return render(request, "frontend/const.html")

def contact(request):
  consuls = Consul.objects.all()
  praetors = Praetor.objects.all()
  quaestors = Quaestor.objects.all()
  aediles = Aedile.objects.all()
  return render(request, "frontend/contact.html", {"consuls": consuls, "praetors": praetors, "quaestors": quaestors, "aediles": aediles})

