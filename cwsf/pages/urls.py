from django.urls import path
from .views import HomePageView, NotebookPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("notebook/", NotebookPageView.as_view(), name="notebook"),
]
