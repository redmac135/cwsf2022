from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

from .models import Person
from .serializers import PersonSerializer

from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.


class HomePageView(View):
    template_name = "pages/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'people': Person.get()})


class NotebookPageView(TemplateView):
    template_name = "pages/notebook.html"


class GuidePageView(TemplateView):
    template_name = "pages/guide.html"


class AccomplishmentsView(TemplateView):
    template_name = "pages/accomplishments.html"


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = "name"

    def retrieve(self, request, name=None, *args, **kwargs):
        queryset = self.queryset
        user = get_object_or_404(queryset, name=name)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
