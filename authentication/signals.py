from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # Check if the user is a regular user (not superuser or staff)
    if created and not instance.is_superuser and not instance.is_staff:
        # Create profile for new regular user
        Profile.objects.create(user=instance)
        