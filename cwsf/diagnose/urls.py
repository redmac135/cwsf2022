from django.urls import path
from .views import DiagnoseView, tmp_success

urlpatterns = [
    path('', DiagnoseView.as_view(), name='home'),
    path('success', tmp_success) 
]