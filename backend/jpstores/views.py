from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from jpstores.models import Category, Product, PurchaseHistory
from jpstores.serializers import (
    CategorySerializer,
    ProductSerializer,
    PurchaseHistorySerializer,
)
from jpstores.utils import custom_paginate


# Create your views here.


class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all().order_by("id")
    serializer_class = CategorySerializer

    @action(detail=True, url_name="products", serializer_class=ProductSerializer)
    def products(self, request, pk=None):
        products = Product.objects.filter(category=pk)

        return custom_paginate(self, products)


class PurchaseHistoryViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = PurchaseHistory.objects.all().order_by("id")
    serializer_class = PurchaseHistorySerializer

    def list(self, request, *args, **kwargs):
        print("USER", request.user.id)
        user = request.user.id
        purchase_history = self.queryset.filter(user=2)

        return custom_paginate(self, purchase_history)
