from .forms import DiagnoseForm
from django.views.generic.edit import FormView


# Create your views here.
class DiagnoseView(FormView):
    template_name = 'diagnose/index.html'
    form_class = DiagnoseForm