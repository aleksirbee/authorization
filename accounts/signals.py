
# It is necessary to ensure that a profile is created automatically when a new user is created. That's why this file is created - the Signal

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User) # The post_save signal will create the profile after a new user is created.
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)