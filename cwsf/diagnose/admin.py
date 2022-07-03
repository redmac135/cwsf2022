from django.contrib import admin
from .models import DiagnoseModel, GenelabModel

# Register your models here.
admin.site.register(DiagnoseModel)
admin.site.register(GenelabModel)
