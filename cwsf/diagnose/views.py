from django import views
from django.shortcuts import render, redirect
from .forms import DiagnoseForm
from django.views.generic import View

from .utils import parse_file

# Create your views here.
class DiagnoseView(View):
    template_name = 'diagnose/index.html'
    form_class = DiagnoseForm
    success_url = '/success'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            parse_file(request.FILES['file'])
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})

def tmp_success(request):
    return render(request, 'diagnose/success.html', {})
