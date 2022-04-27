from django.shortcuts import render, get_list_or_404

# Create your views here.
from .models import Link

def links(request):
    links = get_list_or_404(Link)
    return render(request, 'links/links.html', {
        'links': links
        })