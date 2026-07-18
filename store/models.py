from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Bike(models.Model):
    STOCK_AVAILABLE = "available"
    STOCK_LIMITED = "limited"
    STOCK_OUT = "out_of_stock"
    STOCK_CHOICES = [
        (STOCK_AVAILABLE, "Available"),
        (STOCK_LIMITED, "Limited Stock"),
        (STOCK_OUT, "Out of Stock"),
    ]

    name = models.CharField(max_length=150)
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="bikes")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="bikes")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    specifications = models.TextField(blank=True)
    stock_status = models.CharField(max_length=20, choices=STOCK_CHOICES, default=STOCK_AVAILABLE)
    stock_quantity = models.PositiveIntegerField(default=0)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.name} ({self.model})"
    
class BikeImage(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="bike_images/")
    is_primary = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.bike}"


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name="reviews")
    customer_name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating}★ by {self.customer_name} on {self.bike}"