from django.urls import path
from . import views

urlpatterns = [
    path('organizations/', views.index, name='organizations'),   # Stránka organizací
    path('fighters/', views.fighters, name='fighters'),          # Stránka zápasníků
]