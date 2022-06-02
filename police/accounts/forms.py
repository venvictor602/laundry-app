from django.forms import ModelForm
from django import forms
from .models import *


class ApplicationForm(ModelForm):
    class Meta:
        model = Candidates
        fields = '__all__'