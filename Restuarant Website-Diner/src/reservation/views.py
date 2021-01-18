from .models import Reservation
from django.shortcuts import render
from .forms import ReserveTableForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
# Create your views here.

def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()
            messages.success(request, 'Your reservation was successfull !')
            reserve_form = ReserveTableForm()
        else:
            messages.warning(request, 'Please correct the error below.') 


    context ={'reserve_form' :reserve_form}
    return render(request,'Reservation/reservation.html',context)