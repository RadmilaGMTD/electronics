from django.core.exceptions import ValidationError


class SupplierValidator:
    def __call__(self, supplier):
        """
        Валидация иерархии поставщиков
        """
        if supplier.type == "factory":
            if supplier.suppliers:
                raise ValidationError("Завод не может иметь поставщиков")
            if supplier.debt != 0:
                raise ValidationError("Завод не может иметь задолженность")
            return

        if supplier.suppliers:
            if supplier.type == "entrepreneur" and supplier.suppliers.type == "entrepreneur":
                raise ValidationError("ИП не может закупать у другого ИП")
            if supplier.type == "retail" and supplier.suppliers.type == "entrepreneur":
                raise ValidationError("Розничная сеть не может закупать у ИП")

        if supplier.level > 2:
            raise ValidationError("Максимальная глубина иерархии - 3 уровня (0-2)")
