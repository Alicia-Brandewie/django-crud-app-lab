from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Horse, Feeding
from .forms import FeedingForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.



class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def horse_index(request):
    horses = Horse.objects.filter(user=request.user)
    return render(request, 'horses/index.html', {'horses': horses})

@login_required
def horse_detail(request, horse_id):
    horse = Horse.objects.get(id=horse_id)
    return render(request, 'horses/detail.html', {
        'horse': horse,'feeding_form': FeedingForm
    })


class HorseCreate(LoginRequiredMixin, CreateView):
    model = Horse
    fields = ['name', 'breed','description', 'age', 'nickname']
    # success_url = '/horses/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class HorseUpdate(LoginRequiredMixin, UpdateView):
    model = Horse
    fields = ['breed', 'description', 'age', 'nickname']

class HorseDelete(LoginRequiredMixin, DeleteView):
    model = Horse
    success_url = '/horses/'

@login_required
def add_feeding(request, horse_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.horse_id = horse_id
        new_feeding.save()
    return redirect('horse-detail', horse_id=horse_id)

@login_required
def update_feeding(request, horse_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        update_feeding = form.save(commit=False)
        update_feeding.horse_id = horse_id
        update_feeding.save()
    return redirect('horse-detail', horse_id=horse_id)


class FeedingCreate(LoginRequiredMixin, CreateView):
    model= Feeding
    fields='__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class FeedingUpdate(LoginRequiredMixin, UpdateView):
    model = Horse
    fields ='__all__'

class FeedingDelete(LoginRequiredMixin, UpdateView):
    model = Horse
    success_url = 'horses/<int:horse_id>/'


@login_required
def delete_feeding(request, horse_id):
    form = FeedingForm(request.DELETE)
    if form.is_valid():
        delete_feeding = form.save(commit=False)
        delete_feeding.horse_id = horse_id
        delete_feeding.save()
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