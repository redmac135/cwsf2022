from django import forms
from django.forms import ModelForm
from .models import DiagnoseModel


class DiagnoseForm(ModelForm):
    class Meta:
        model = DiagnoseModel
        fields = ["upload"]
