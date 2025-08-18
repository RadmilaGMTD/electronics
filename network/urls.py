from django.urls import path

from users.apps import UsersConfig

from .views import SupplierCreateView, SupplierDetailView, SupplierListApiView

app_name = UsersConfig.name

urlpatterns = [
    path("", SupplierListApiView.as_view(), name="suppliers_list"),
    path("create/", SupplierCreateView.as_view(), name="suppliers_create"),
    path("suppliers/<int:pk>/", SupplierDetailView.as_view(), name="suppliers_detail"),
]
