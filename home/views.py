from django.shortcuts import render

# Create your views here.
def index(request):
    """Display the home page"""
    return render(request, 'home/index.html')