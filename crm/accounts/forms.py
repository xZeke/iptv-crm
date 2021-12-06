from django.db.models.fields import CharField
from django.forms import ModelForm, DateInput
from django.forms.widgets import NumberInput, TextInput

from .models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['expires']
        widgets = {
            'expires': DateInput(attrs={'type': 'date', 'class': 'form-control mb-2 mr-sm-2 mb-sm-0'})
        }

class NewCustomer(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['date_created', 'needs_remind']
        widgets ={
            'name': TextInput(attrs={'class': 'form-control', 'style': 'max-width: 300px'}),
            'account_name': TextInput(attrs={'class': 'form-control','style': 'max-width: 300px'}), 
            'payment_name': TextInput(attrs={'class': 'form-control','style': 'max-width: 300px'}), 
            'number_of_boxes': NumberInput(attrs={'class': 'form-control','style': 'max-width: 300px'}), 
            'server': TextInput(attrs={'class': 'form-control','style': 'max-width: 300px'}), 
            'mac_address': TextInput(attrs={'class': 'form-control','style': 'max-width: 300px'}), 
            'expires': DateInput(attrs={'type': 'date', 'class': 'form-control mb-2 mr-sm-2 mb-sm-0','style': 'max-width: 300px'}), 
            'communication': TextInput(attrs={'class': 'form-control','style': 'max-width: 300px'}), 
            'referal': TextInput(attrs={'class': 'form-control','style': 'max-width: 300px'}), 
            'building_type': TextInput(attrs={'class': 'form-control','style': 'max-width: 300px'}),  
            'address': TextInput(attrs={'class': 'form-control','style': 'max-width: 300px'}), 
            'customer_since': DateInput(attrs={'type': 'date', 'class': 'form-control mb-2 mr-sm-2 mb-sm-0','style': 'max-width: 300px'}), 
            'notes': TextInput(attrs={'class': 'form-control','style': 'max-width: 300px'}),
        }
    def clean_rowname(self):
        return self.cleaned_data['rowname'] or None