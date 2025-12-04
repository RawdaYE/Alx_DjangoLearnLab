from django.db.models.signals import post_save
from django.contrib.auth.models import User
from relationship_app.models import UserProfile
from django.dispatch import receiver


@receiver(post_save, sender=User)

def createUserProfile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

