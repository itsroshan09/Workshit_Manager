# rws_app/forms.py
from django import forms
from .models import Work, Bill

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = '__all__'
        widgets = {
            'order_details': forms.TextInput(attrs={'placeholder': 'e.g., RWS/T/RR/115/2022 Dt.10/06/2022'}),
        }

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        exclude = ['work'] # The work is assigned automatically in the view
        widgets = {
            'bill_date': forms.DateInput(attrs={'type': 'date'}),
            'financial_year': forms.TextInput(attrs={'placeholder': 'e.g., 2024-25'}),
        }