from django.urls import path
from .views import (
    HomePageView,
    NotebookPageView,
    GuidePageView,
    AccomplishmentsView,
    PersonViewSet,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("notebook/", NotebookPageView.as_view(), name="notebook"),
    path("guide/", GuidePageView.as_view(), name="guide"),
    path("accomplishments/", AccomplishmentsView.as_view(), name="accomplishments"),
    path("api/person/<str:name>", PersonViewSet.as_view({"get": "retrieve"})),
]
