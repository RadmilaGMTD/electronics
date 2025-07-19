from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Product, Supplier


@admin.register(Supplier)
class SuppliersAdmin(admin.ModelAdmin):
    list_filter = ("contacts__city",)
    list_display = ("name", "type", "debt", "get_supplier_link", "level")
    actions = ["clear_debt"]

    def clear_debt(self, request, queryset):
        updated = queryset.update(debt=0)
        self.message_user(request, f"Очищена задолженность для {updated} поставщиков")

    clear_debt.short_description = "Очистить задолженность перед поставщиком"

    def get_supplier_link(self, obj):
        if obj.suppliers:
            url = reverse("admin:network_supplier_change", args=[obj.suppliers.id])
            return format_html('<a href="{}">{}</a>', url, obj.suppliers.name)
        return "-"

    get_supplier_link.short_description = "Поставщик"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "release_date")
