from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=16)
    image = models.CharField(max_length=32)
    summary = models.CharField(max_length=2048)

    def __str__(self) -> str:
        return self.name

    @classmethod
    def get(cls):
        return cls.objects.all()
