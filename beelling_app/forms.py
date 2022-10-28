from django.forms import ModelForm
from beelling_app.models import Bill

class BillForm(ModelForm):
    class Meta:
        model = Bill
        fields = ['Name', 'Value', 'DueDate', 'Category', 'IsActive']