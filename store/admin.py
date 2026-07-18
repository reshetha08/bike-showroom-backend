from django.contrib import admin
from .models import Brand, Category, Bike, BikeImage, Review

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Bike)
admin.site.register(BikeImage)
admin.site.register(Review)