from django.urls import path
from .views import DiagnoseView, success

urlpatterns = [
    path('', DiagnoseView.as_view(), name='home'),
]