from django import views
from django.shortcuts import render, redirect
from .forms import DiagnoseForm
from django.views.generic import View

from .utils import parse_file

# Create your views here.
class DiagnoseView(View):
    template_names = ['diagnose/index.html', 'diagnose/success.html']
    form_class = DiagnoseForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_names[0], {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            try:
                results = parse_file(request.FILES['file'])
            except ValueError:
                return redirect('valueError')
            labels = [x[0] for x in results]
            output = [x[1] for x in results]
            return render(request, self.template_names[1], {'labels': labels, 'output': output})
        else:
            return render(request, self.template_names[0], {'form': form})

def valueError(request):
    return render(request, 'diagnose/valueError.html', {})
