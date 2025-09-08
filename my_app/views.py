from django.shortcuts import render

class Horse:
    def __init__(self, name, breed, description, age, nickname):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
        self.nickname = nickname

horses = [
    Horse('Chad', 'Quarter Horse', 'Western Pleasure speed, Jumper jump', 6, 'Mojo Dojo Casa Horse'),
    Horse('Raven', 'Thoroughbred', 'Terrifying', 8, 'Rave-gravy'),
]


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def horse_index(request):
    return render(request, 'horses/index.html', {'horses': horses})