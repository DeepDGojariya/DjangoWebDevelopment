from django import forms
from .models import Reserve

class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields ='__all__'
        
'''
class ReserveForm(forms.ModelForm):
    to_email = forms.EmailField(diabled=True)
    class Meta:
        model = Reserve
        fields = '__all__'
'''