from dataclasses import field
from django.forms import ModelForm
from django import forms
from beelling_app.models import Bill

class BillForm(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    Value = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 9999999}))
    DueDate = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y', attrs={"class": "form-control"}), input_formats=('%d/%m/%Y', ))
    Category = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model = Bill
        fields = ['Name', 'Value', 'DueDate', 'Category', 'IsActive']
