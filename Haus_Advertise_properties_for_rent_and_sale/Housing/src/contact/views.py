from django.shortcuts import render,redirect
from .models import ContactDetails
from .forms import ContactForm
from django.core.mail import BadHeaderError
from django.core.mail import send_mail,EmailMessage
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.conf import settings

# Create your views here.
def send_mail(request):
    contact_details = ContactDetails.objects.last()
    template = 'contact/contact.html'

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data.get('subject')
            from_email = contact_form.cleaned_data.get('from_email')
            message = contact_form.cleaned_data.get('message')
            msg = EmailMessage(subject,message,from_email,[settings.EMAIL_HOST_USER])
            msg.send()
            #Alternative.
            #send_mail(subject,message,from_email,[settings.EMAIL_HOST_USER])
            '''try:
                
            except BadHeaderError:
                return HttpResponse('Invalid Header')'''
            contact_form = ContactForm()
            messages.add_message(request, messages.SUCCESS, 'Thanks for your feedback.')
            #return redirect('contact:success')

    else:
        contact_form = ContactForm()
    context = {
        'contact_details':contact_details,
        'contact_form':contact_form
    }
    return render(request,template,context)


def succuss(request):
    return HttpResponse('Message Sent Successfully')