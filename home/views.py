from django.shortcuts import render
from .models import Structure


def index(request):
    return render(
        request,
        "index.html",
        {"structure": Structure.objects.all()})
