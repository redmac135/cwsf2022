from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class NotebookPageView(TemplateView):
    template_name = "pages/notebook.html"
