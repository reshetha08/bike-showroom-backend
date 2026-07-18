from django.db.models import Avg
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Review


def update_bike_rating(bike):
    avg = bike.reviews.aggregate(avg=Avg('rating'))['avg'] or 0
    bike.avg_rating = round(avg, 2)
    bike.save(update_fields=['avg_rating'])


@receiver(post_save, sender=Review)
def review_saved(sender, instance, **kwargs):
    update_bike_rating(instance.bike)


@receiver(post_delete, sender=Review)
def review_deleted(sender, instance, **kwargs):
    update_bike_rating(instance.bike)