from django.urls import path
from .views import (
    DiagnoseView,
    GenelabView,
    valueError,
    downloadFile,
    diagnose_file,
    genelab_file,
)

urlpatterns = [
    path("error", valueError, name="valueError"),
    path("diagnose", DiagnoseView.as_view(), name="diagnose"),
    path("genelab", GenelabView.as_view(), name="genelab"),
    path("diagnose/<str:filename>", diagnose_file, name="diagnose_file"),
    path("genelab/<str:filename>", genelab_file, name="genelab_file"),
    path("download/<str:filename>", downloadFile, name="download"),
]
