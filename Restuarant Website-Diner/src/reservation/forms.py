from django import forms
from .models import Reservation
from bootstrap_datepicker_plus import DatePickerInput



class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        
        fields = '__all__'
        widgets = {
            #'Date': DatePickerInput(format='%Y-%m-%d'), # default date-format %m/%d/%Y will be used.
            'Date': DateInput(),
            'time':TimeInput()
            
        }
