from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, CategoryViewSet, BikeViewSet, BikeImageViewSet, ReviewViewSet

router = DefaultRouter()
router.register('brands', BrandViewSet)
router.register('categories', CategoryViewSet)
router.register('bikes', BikeViewSet)
router.register('bike-images', BikeImageViewSet)
router.register('reviews', ReviewViewSet, basename='review')

urlpatterns = router.urls