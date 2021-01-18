from django.shortcuts import render
from .models import AboutUs,WhyChooseUs,Chef
# Create your views here.
def aboutus_list(request):
    about = AboutUs.objects.all()
    why_choose_us = WhyChooseUs.objects.last()
    chef = Chef.objects.all()
    

    context ={
        'about': about,
        'why_choose_us':why_choose_us,
        'chef':chef
    }
    return render(request,'aboutus/about.html',context)
