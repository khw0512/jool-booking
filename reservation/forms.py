from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['client', 'month', 'day', 'hour', 'minute', 'desc']
        widgets = {
            'client': forms.TextInput(attrs={'class': 'form-control'}),
            'month': forms.NumberInput(attrs={'class': 'form-control'}),
            'day': forms.NumberInput(attrs={'class': 'form-control'}),
            'hour': forms.NumberInput(attrs={'class': 'form-control'}),
            'minute': forms.NumberInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            "client": "예약자",
        }
