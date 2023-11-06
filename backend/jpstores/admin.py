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
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "phone",
        "is_active",
        "is_staff",
        "date_joined",
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "price",
        "rating",
        "stock",
        "brand",
        "category",
    )


class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "image_url",
        "thumbnail_url",
    )


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "user",
        "comment",
        "rating",
        "date_added",
    )


class PurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "user",
        "purchase_date",
        "quantity",
        "total",
        "status",
    )


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(PurchaseHistory, PurchaseHistoryAdmin)
