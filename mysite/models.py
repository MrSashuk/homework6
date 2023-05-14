from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    




class Phone(models.Model):
    model = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(blank=True)

    def __str__(self) -> str:
        return self.model