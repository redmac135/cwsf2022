from django.db import models

# Create your models here.
class DiagnoseModel(models.Model):
    unique = models.CharField(max_length=64)
    upload = models.FileField(upload_to='media')