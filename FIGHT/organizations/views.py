from django.shortcuts import render
from .models import Fighter  # <-- DŮLEŽITÝ IMPORT

def index(request):
    return render(request, 'organizations/index.html')

def fighters(request):
    fighters = Fighter.objects.all()
    return render(request, 'organizations/fighters.html', {'fighters': fighters})