from django.urls import path
from . import views

app_name = 'addproperty'

urlpatterns = [
   path('',views.add_property,name = 'add_property')
   
]