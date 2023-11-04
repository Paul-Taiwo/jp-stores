from django.contrib import admin
from .models import (
    Category,
    Product,
    ProductImage,
    ProductReview,
    PurchaseHistory,
    User,
)

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(PurchaseHistory)
