from django.contrib import admin
#from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

from .models import Meals,Category
#class MealsAdmin(SummernoteModelAdmin):
   # summernote_fields = '__all__'

admin.site.register(Meals),#MealsAdmin)
admin.site.register(Category)