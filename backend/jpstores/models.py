from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = CloudinaryField("image")
    age = models.PositiveIntegerField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    GenderChoice = (
        ("M", "Male"),
        ("F", "Female"),
    )
    gender = models.CharField(
        max_length=10, choices=GenderChoice, blank=True, null=True
    )

    # Address
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)

    # Bank Information
    card_expire = models.CharField(max_length=7, blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    card_type = models.CharField(max_length=20, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    iban = models.CharField(max_length=24, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.username}"


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image_url = CloudinaryField("image")
    thumbnail_url = CloudinaryField("image")


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, default=0, blank=True, null=True
    )
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField()
    brand = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ManyToManyField(ProductImage)

    def __str__(self):
        return f"{self.title}: {self.description}"


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.title}"


class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    StatusChoices = (
        ("Pending", "Pending"),
        ("Fulfilled", "Fulfilled"),
    )
    status = models.CharField(max_length=10, choices=StatusChoices)

    def __str__(self):
        return f"Purchase by {self.user.username} on {self.purchase_date}"
