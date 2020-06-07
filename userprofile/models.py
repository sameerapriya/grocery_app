from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    address = models.CharField(max_length=225, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    postal_code = models.CharField(max_length=50, blank=True, null=True)
    phone = PhoneField(blank=True, help_text='Contact Phone Number')

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=get_user_model())
def create_profile(instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
