from django.shortcuts import render,redirect
from .forms import AddProperty
from django.contrib import messages
# Create your views here.
def add_property(request):
    template = 'addproperty/add_property.html'
    message=''
    if request.method == 'POST':
        property_form = AddProperty(request.POST,request.FILES)
        if property_form.is_valid():
          property_form.save()
          messages.add_message(request, messages.SUCCESS, 'Thanks for adding this property you can view this property once the admin approves it.')
          return redirect('http://127.0.0.1:8000/add-property')
    else:
        print("invalid")
        property_form = AddProperty()
    context = {
        'property_form':property_form,
        
    }
    return render(request,template,context)
    
