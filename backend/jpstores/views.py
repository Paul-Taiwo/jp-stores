import rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from jpstores.models import Category, Product
from jpstores.serializers import CategorySerializer, ProductSerializer


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
        page = self.paginate_queryset(products)

        if page is not None:
            serializers = self.get_serializer(page, many=True, read_only=True)
            return self.get_paginated_response(serializers.data)

        serializers = self.get_serializer(products, many=True, read_only=True)
        return Response(serializers.data, HTTP_200_OK)
