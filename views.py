from django.shortcuts import render
from .models import place, team

def index(request):
    obj = place.objects.all()
    tm = team.objects.all()
    context = {
        'result': obj,
        'res': tm
    }
    return render(request, "index.html", context)
