from django.shortcuts import render

# Create your views here.
from .models import Link

def links(request):
    return render(request, 'links/links.html')