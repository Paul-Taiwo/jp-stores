from rest_framework import serializers

from .models import Product, ProductImage, ProductReview, User


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

    def to_representation(self, product):
        representation = super().to_representation(product)

        if self.context["request"].resolver_match.url_name == "products-detail":
            reviews_data = ProductReview.objects.filter(product=product)
            reviews_serializer = ProductReviewSerializer(reviews_data, many=True)
            representation["reviews"] = reviews_serializer.data

        return representation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "is_superuser",
            "is_active",
            "is_staff",
            "groups",
            "user_permissions",
        ]


class ProductReviewUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        exclude = UserSerializer.Meta.exclude + [
            "age",
            "gender",
            "last_login",
            "email",
            "birth_date",
            "phone",
            "address",
            "city",
            "lat",
            "lng",
            "postal_code",
            "state",
            "card_expire",
            "card_number",
            "card_type",
            "currency",
            "iban",
            "date_joined",
        ]


class ProductReviewSerializer(serializers.ModelSerializer):
    user = ProductReviewUserSerializer(read_only=True)

    class Meta:
        model = ProductReview
        fields = "__all__"
