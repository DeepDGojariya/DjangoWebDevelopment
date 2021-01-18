from django.shortcuts import render
from .models import Property,Category
from .forms import ReserveForm
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def property_list(request):
    property_list = Property.objects.all()
    print(property_list)
    template = 'property/list.html'
    search_query = request.GET.get('q')
    if search_query:
        search_query = search_query.split(' ')
        cities = ['mumbai','bengeluru','bangalore','hyderabad','kolkata','delhi']
        index=0
        for i,word in enumerate(search_query):
            if word.lower() in cities:
                index = i
                break
    property_type = request.GET.get('property_type')
    if search_query and property_type:
        property_list = property_list.filter(
            (Q(description__icontains = search_query[0]) &
            Q(location__icontains = search_query[index])) &
            Q(type_of_property__icontains =property_type[0])
        ).distinct()
    context = {
        'property_list':property_list
    }
    return render(request,template,context)

def property_detail(request,id):
    property_detail = Property.objects.get(id=id)
    template = 'property/detail.html'
    reciever_email = property_detail.email
    owner_name = property_detail.owner_name
    rent = property_detail.type_of_property
    if rent=='sale':
        rent = 'buy'
    
    if request.method == 'POST': 
        reserve_form = ReserveForm(request.POST)
        
        if reserve_form.is_valid():
            client_name = reserve_form.cleaned_data.get('name')
            client_email = reserve_form.cleaned_data.get('email')
            subject = 'Someone showed Interest in your Property'
            message = 'Hi '+owner_name+','+'\n'+'We would like to inform you that our client '+client_name+' has shown interest in your property and would like to '+rent+' your property.'+'\n'+'You can contact the client and finalize a deal.'+'\n'+'Contact-Details :'+'\n'+'client-email: '+client_email
            send_mail(subject,message,settings.EMAIL_HOST_USER,[reciever_email],fail_silently=False)
            reserve_form.save()
            messages.add_message(request, messages.SUCCESS, 'We have sent a mail to the property owner.He/She will get in touch with you soon.')
            reserve_form = ReserveForm()
    else:
        reserve_form = ReserveForm()

    context = {
        'property_detail':property_detail,
        'reserve_form':reserve_form
    }
    return render(request,template,context)
    