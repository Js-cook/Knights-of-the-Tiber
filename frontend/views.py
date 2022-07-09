from django.shortcuts import render
from student_portal.models import Consul, Praetor, Quaestor, Aedile
import random

# Create your views here.
def index(request):
  consuls = Consul.objects.all()
  praetors = Praetor.objects.all()
  quaestors = Quaestor.objects.all()
  aediles = Aedile.objects.all()
  quote = random.choice(list(open("frontend/static/quotes.txt")))
  return render(request, "frontend/index.html", {"consuls": consuls, "praetors": praetors, "quaestors": quaestors, "aediles": aediles, "quote": quote})

def constitution(request):
  return render(request, "frontend/const.html")

def contact(request):
  consuls = Consul.objects.all()
  praetors = Praetor.objects.all()
  quaestors = Quaestor.objects.all()
  aediles = Aedile.objects.all()
  return render(request, "frontend/contact.html", {"consuls": consuls, "praetors": praetors, "quaestors": quaestors, "aediles": aediles})

def news(request):
  return render(request, "frontend/news.html")

def club_news(request):
  return render(request, "frontend/cnews.html")
