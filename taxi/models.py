from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return f"{self.username}"


class Car(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(to=Driver)

    def __str__(self) -> str:
            return f"{self.model}"
