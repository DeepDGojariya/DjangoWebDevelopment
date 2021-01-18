from django import forms
from property.models import Property

class AddProperty(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['owner_name','email','description','location','type_of_property',
                  'price','area','category','beds_number','baths_number','garages_number','image']