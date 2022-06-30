from django.db import models

# Create your models here.
class DiagnoseModel(models.Model):
    upload = models.FileField()
