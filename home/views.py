from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def category(request):
    return render(request, 'category.html')


def single(request):
    return render(request, 'single.html')
