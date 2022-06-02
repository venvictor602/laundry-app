from django.forms import ModelForm
from django import forms
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'