from rest_framework import serializers

from .models import Product, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(
        read_only=True,
    )
    images = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"
        ordering = ["-id"]

    def product_images(self, product):
        images = ProductImage.objects.filter(product=product)
        return images

    def get_images(self, product):
        images = self.product_images(product)
        image_data = []

        for image in images:
            image_data.append(image.image_url)
        return image_data

    def get_thumbnail(self, product):
        images = self.product_images(product).first()

        return images.thumbnail_url
