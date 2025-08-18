from django.db import models

from users.models import User

from .validators import SupplierValidator


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название продукта")
    model = models.CharField(max_length=50, verbose_name="Модель продукта")
    release_date = models.DateField(verbose_name="Дата выхода продукта на рынок")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name}"


class Supplier(models.Model):
    TYPE_CHOICES = [("factory", "Завод"), ("retail", "Розничная сеть"), ("entrepreneur", "предприниматель")]
    type = models.CharField(choices=TYPE_CHOICES, verbose_name="Тип", default="factory")
    name = models.CharField(max_length=50, verbose_name="Название")
    contacts = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Контакт")
    products = models.ManyToManyField(Product, verbose_name="Продукт")
    suppliers = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Поставщик")
    debt = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="Задолженность перед поставщиком"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    level = models.PositiveIntegerField(editable=False, verbose_name="Уровень")

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if self.type == "factory":
            self.level = 0
            self.suppliers = None
        else:
            if self.suppliers:
                self.level = self.suppliers.level + 1
            else:
                self.level = 1 if self.type == "retail" else 2

        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        validator = SupplierValidator()
        validator(self)
        super().clean()
