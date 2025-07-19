from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    city = models.CharField(max_length=50, verbose_name="Город")
    country = models.CharField(max_length=50, verbose_name="Страна")
    street = models.CharField(max_length=50, verbose_name="Улица")
    house_number = models.CharField(max_length=50, verbose_name="Номер дома")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
