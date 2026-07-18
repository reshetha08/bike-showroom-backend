from rest_framework import serializers
from .models import Brand, Category, Bike, BikeImage, Review


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class BikeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeImage
        fields = ['id', 'bike', 'image', 'is_primary']


class BikeSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    images = BikeImageSerializer(many=True, read_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(), source='brand', write_only=True
    )
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Bike
        fields = [
            'id', 'name', 'model', 'brand', 'category', 'brand_id', 'category_id', 'price',
            'description', 'specifications', 'stock_status',
            'stock_quantity', 'avg_rating', 'is_active', 'created_at',
            'images',
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'bike', 'customer_name', 'rating', 'comment', 'is_approved', 'created_at']
        read_only_fields = ['is_approved']