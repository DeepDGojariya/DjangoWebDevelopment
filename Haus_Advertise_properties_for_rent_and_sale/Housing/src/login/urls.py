from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('',views.registration_view,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('login/',views.login_view,name='login')
]