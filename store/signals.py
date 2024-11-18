from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Customer  # Import the Customer model

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_custom_profile(sender, instance, created, **kwargs):
    if created:  # Check if a new user is being created
        Customer.objects.create(user=instance)  # Create a Customer profile
#از رو یوزر ی کاستومر یوزر میسازه 