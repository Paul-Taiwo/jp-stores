from rest_framework.viewsets import ModelViewSet

from jpstores.models import Product
from jpstores.serializers import ProductSerializer


# Create your views here.


class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = ProductSerializer
