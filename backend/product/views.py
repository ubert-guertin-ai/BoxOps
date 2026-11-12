from typing import Any
from django.db.models import QuerySet
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Product] = Product.objects.all()
    serializer_class: type[ProductSerializer] = ProductSerializer
    lookup_field: str = "uuid"
    authentication_classes: list[Any] = []
    lookup_value_regex: str = (
        "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
    )
