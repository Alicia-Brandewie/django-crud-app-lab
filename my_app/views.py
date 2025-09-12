from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Horse
from .forms import FeedingForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.



class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def horse_index(request):
    horses = Horse.objects.all()
    return render(request, 'horses/index.html', {'horses': horses})

def horse_detail(request, horse_id):
    horse = Horse.objects.get(id=horse_id)
    return render(request, 'horses/detail.html', {
        'horse': horse,'feeding_form': FeedingForm
    })


class HorseCreate(CreateView):
    model = Horse
    fields = ['name', 'breed','description', 'age', 'nickname']
    # success_url = '/horses/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class HorseUpdate(UpdateView):
    model = Horse
    fields = ['breed', 'description', 'age', 'nickname']

class HorseDelete(DeleteView):
    model = Horse
    success_url = '/horses/'

def add_feeding(request, horse_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.horse_id = horse_id
        new_feeding.save()
    return redirect('horse-detail', horse_id=horse_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )