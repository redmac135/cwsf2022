from django.urls import path
from .views import HomePageView, MatrixPageView, NotebookPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('notebook/', NotebookPageView.as_view(), name='notebook'),
    path('matrix/', MatrixPageView.as_view(), name='matrix'),
]