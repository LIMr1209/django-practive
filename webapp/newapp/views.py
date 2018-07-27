from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(15)
def index(request):
    print('enter into index')
    return render(request, 'index.html')
