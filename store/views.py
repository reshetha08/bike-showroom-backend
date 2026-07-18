from rest_framework import viewsets
from .models import Brand, Category, Bike, BikeImage, Review
from .serializers import (
    BrandSerializer, CategorySerializer, BikeSerializer,
    BikeImageSerializer, ReviewSerializer,
)
from .permissions import IsAdminOrReadOnly, ReviewPermission


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    permission_classes = [IsAdminOrReadOnly]


class BikeImageViewSet(viewsets.ModelViewSet):
    queryset = BikeImage.objects.all()
    serializer_class = BikeImageSerializer
    permission_classes = [IsAdminOrReadOnly]


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [ReviewPermission]

    def get_queryset(self):
        queryset = Review.objects.all()
        bike_id = self.request.query_params.get('bike')
        if bike_id:
            queryset = queryset.filter(bike=bike_id)
        return queryset