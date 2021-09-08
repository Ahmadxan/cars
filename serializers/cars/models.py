from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Madel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    position = models.PositiveIntegerField()

    def __str__(self):
        return self.name