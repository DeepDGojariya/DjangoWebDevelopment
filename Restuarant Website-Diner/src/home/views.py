from django.shortcuts import render
from Meals.models import Meals,Category
from blog.models import Post
# Create your views here.
def home(request):
    meal = Meals.objects.all()[0:6]
    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()[0:3]
    posts2 = Post.objects.all()[3:]  
    
   
    context ={
        'meals':meal,
        'categories':categories,
        'meal_list':meal_list,
        'posts':posts,
        'posts2':posts2
        
        
    }
    return render(request,'home/home.html',context)