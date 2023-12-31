"""
URL configuration for jpstores project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconfxP
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from jpstores.views import CategoryViewSet, ProductsViewSet, PurchaseHistoryViewSet


router = DefaultRouter()

router.register(r"products", ProductsViewSet, basename="products")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(
    r"purchase-history", PurchaseHistoryViewSet, basename="purchase-history"
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(r"api/", include(router.urls)),
]
