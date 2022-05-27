from django.urls import path
from .views import DiagnoseView, valueError

urlpatterns = [
    path('', DiagnoseView.as_view(), name='home'),
    path('error', valueError, name='valueError')
]