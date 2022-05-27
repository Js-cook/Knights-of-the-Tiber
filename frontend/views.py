from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, "frontend/index.html")

def constitution(request):
  return render(request, "frontend/const.html")

def contact(request):
  return render(request, "frontend/contact.html")