from django.shortcuts import render
from .models import Horse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def horse_index(request):
    horses = Horse.objects.all()
    return render(request, 'horses/index.html', {'horses': horses})