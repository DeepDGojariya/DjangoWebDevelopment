from django.contrib import admin
from .models import Property,Category,Reserve
# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['description','type_of_property','category','area','price']
    search_fields = ['description','type_of_property']
    list_filter = ['category']

admin.site.register(Property,PropertyAdmin)
admin.site.register(Category)
admin.site.register(Reserve)

