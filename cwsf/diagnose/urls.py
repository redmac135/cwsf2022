from django.urls import path
from .views import DiagnoseView, GenelabView, valueError, downloadFile, exampleView

urlpatterns = [
    path("", DiagnoseView.as_view(), name="home"),
    path("genelab", GenelabView.as_view(), name="genelab"),
    path("example/<str:filename>", exampleView, name="exampleView"),
    path("error", valueError, name="valueError"),
    path("download/<str:filename>", downloadFile, name="download"),
]
