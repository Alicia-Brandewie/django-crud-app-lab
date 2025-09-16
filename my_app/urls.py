from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # Routes will be added here
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('horses/', views.horse_index, name='horse-index'),
    path('horses/<int:horse_id>/', views.horse_detail, name='horse-detail'),
    path('horses/create/', views.HorseCreate.as_view(), name='horse-create'),
    path('horses/<int:pk>/update/', views.HorseUpdate.as_view(), name='horse-update'),
    path('horses/<int:pk>/delete/', views.HorseDelete.as_view(), name='horse-delete'),
    path('horses/<int:horse_id>/add-feeding/', views.add_feeding, name='add-feeding'),

    path('feeding/create/', views.FeedingCreate.as_view(), name='feeding-create'),
    path('feeding/<int:pk>/update/', views.FeedingUpdate.as_view(), name='feeding-update'),
    path('feeding/<int:pk>/delete/', views.FeedingDelete.as_view(), name='feeding-delete'),

    path('accounts/signup/', views.signup, name='signup'),
]