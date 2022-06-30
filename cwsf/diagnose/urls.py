from django.urls import path
from .views import DiagnoseView, MatrixView, valueError, downloadFile

urlpatterns = [
    path('', DiagnoseView.as_view(), name='home'),
    path('error', valueError, name='valueError'),
    path('download/<str:filename>', downloadFile, name='download'),
    path('matrix', MatrixView.as_view(), name='matrix'),
]