from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # Routes will be added here
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('horses/', views.horse_index, name='horse-index'),
    path('horses/<int:horse_id>/', views.horse_detail, name='horse-detail'),
]