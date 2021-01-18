from django.urls import path
from .import views

app_name = 'predict'

urlpatterns = [
    path('',views.city_select,name='city_select'),
    path('price/',views.predict,name='predict_price')
]