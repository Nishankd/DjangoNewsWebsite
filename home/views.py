from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    views = {}  #yo dictionary ho...yesma key ra values haru add gareko ho tala tira, mapping gareko ho
    views['categories'] = Category.objects.all()
    views['all_news'] = News.objects.all()
    views['featured_news'] = News.objects.filter(featured=True)
    views['popular_news'] = News.objects.filter(popular=True)
    views['latest_news'] = News.objects.filter(latest=True)
    views['sliders'] = News.objects.filter(slider=True)

    return render(request,'index.html', views)


def contact(request):
    views = {}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message

        )
        data.save()
        views['message'] = "Success"
    return render(request,'contact.html', views)

def category(request, slug):
    views = {}
    cat_id = Category.objects.get(slug=slug).id
    views['category_name'] = Category.objects.get(slug=slug).name
    views['cat_news'] = News.objects.filter(category_id=cat_id)
    return render(request,'category.html', views)

def single(request, slug):
    views = {}
    views['single_news'] = News.objects.filter(slug=slug)
    return render(request,'single.html', views)