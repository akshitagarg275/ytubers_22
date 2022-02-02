from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import Youtuber

# Create your views here.

def home(request):
    sliders=Slider.objects.all()
    teams=Team.objects.all()
    featured_yt=Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_tubers=Youtuber.objects.order_by('-created_date')
    data={
        'sliders':sliders,
        'teams':teams,
        'featured_yt':featured_yt,
        'all_tubers':all_tubers
    }
    return render(request,'webpages/home.html',data)

def about(request):
    return render(request,'webpages/about.html')

def contact(request):
    return render(request,'webpages/contact.html')

def services(contact):
    return render(request,'webpages/services.html')