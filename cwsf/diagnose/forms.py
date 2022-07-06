from django import forms
from django.forms import ModelForm
from .models import DiagnoseModel, GenelabModel


class DiagnoseForm(ModelForm):
    class Meta:
        model = DiagnoseModel
        fields = ["upload"]


class GenelabForm(ModelForm):
    class Meta:
        model = GenelabModel
        fields = ["upload"]
