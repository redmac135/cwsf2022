from django.urls import path
from .views import HomePageView, NotebookPageView, GuidePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("notebook/", NotebookPageView.as_view(), name="notebook"),
    path("guide/", GuidePageView.as_view(), name="guide"),   
]
