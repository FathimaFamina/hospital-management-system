from django import forms
from .models import Appointment

class DateInput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'

        widgets = {
            'booking_date': DateInput()
        }

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ['p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date']


# class BookingForm(forms.Form):
#     p_name = forms.CharField(max_length=100, label="P name")
#     p_phone = forms.CharField(max_length=15, label="P phone")
#     p_email = forms.EmailField(label="P email")
#     doc_name = forms.CharField(max_length=100, label="Doc name")
#     booking_date = forms.DateField(label="Booking date", widget=forms.DateInput(format='%d-%m-%Y'))
