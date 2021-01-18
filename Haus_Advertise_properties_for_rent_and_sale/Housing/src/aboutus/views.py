from django.shortcuts import render

# Create your views here.
def about_us(request):
    template = 'aboutus/about.html'
    empty='deep'
    context = {'empty':empty}
    return render(request,template,context)
