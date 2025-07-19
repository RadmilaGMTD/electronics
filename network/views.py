from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.validators import ValidationError

from .models import Supplier
from .permissions import IsActiveUser
from .serializers import SupplierSerializer


class SupplierListApiView(generics.ListAPIView):
    queryset = Supplier.objects.all().select_related("contacts", "suppliers").prefetch_related("products")
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["contacts__country"]


class SupplierCreateView(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all().select_related("contacts", "suppliers").prefetch_related("products")
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]

    def perform_update(self, serializer):
        if "debt" in serializer.validated_data:
            current_debt = serializer.instance.debt
            new_debt = serializer.validated_data["debt"]

            if current_debt != new_debt:
                raise ValidationError("Обновление задолженности перед поставщиком запрещено через API")
        super().perform_update(serializer)
