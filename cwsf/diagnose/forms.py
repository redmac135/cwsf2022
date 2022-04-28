from django import forms

class DiagnoseForm(forms.Form):
    file = forms.FileField()