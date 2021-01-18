from django.shortcuts import render
from property.models import Property,Category
from agents.models import Agent
from django.db.models import Count
# Create your views here.
def index(request):
    category_list = Category.objects.annotate(property_count = Count('property')).values('category_name','property_count')
    property_list = Property.objects.all()[0:3]
    agent_list = Agent.objects.all()
    template = 'home/index.html'
    context = {'category_list':category_list,
                'property_list1':property_list,
                'agent_list1':agent_list}

    return render(request,template,context)