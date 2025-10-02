from django.shortcuts import render
from django.core.cache import cache

def home(request):
    mv = cache.get('movie', 'has_expired')

    if mv == 'has_expired':
        # store in cache for 30 seconds
        cache.set('movie', 'Inceptsdfsdfion', 30)
        mv = cache.get('movie')  # fetch immediately

    return render(request, 'home.html', {'movie': mv})
