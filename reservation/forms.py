from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reserv_id','client', 'contact', 'start_date', 'start_time','end_date','end_time','top','bottom','shoes','bag','location','cost','image','desc','status','completed']
        widgets = {
            'reserv_id' : forms.TextInput(attrs={'class': 'form-control'}),
            'client': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'start_time': forms.TimeInput(attrs={'type': 'time','class': 'form-control'}, format='%H:%M'),
            'start_date': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time','class': 'form-control'}, format='%H:%M'),
            'end_date': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'top' : forms.Select(attrs={'class': 'form-control'}),
            'bottom' : forms.Select(attrs={'class': 'form-control'}),
            'shoes' : forms.Select(attrs={'class': 'form-control'}),
            'bag' : forms.Select(attrs={'class': 'form-control'}),
            'location' : forms.TextInput(attrs={'class': 'form-control'}),
            'cost' : forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={"id": "image_field", 'class': 'form-control'}),
            'status' : forms.Select(attrs={'class': 'form-control'}),
            'completed' : forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'reserv_id' : '예약번호',
            'client': '예약자',
            'contact': '연락처',
            'desc': '설명',
            'start_time': '시작시간',
            'start_date': '시작날짜',
            'end_time': '종료시간',
            'end_date': '종료날짜',
            'top' : '상의',
            'bottom' : '하의',
            'shoes' : '운동화',
            'bag' : '휴대폰 파우치',
            'image': '이미지',
            'status' : '상태',
            'completed' : '완료여부',
        }
