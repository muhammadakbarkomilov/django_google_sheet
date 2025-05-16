from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import exelUser
from .utils import append_data_to_sheet

@receiver(post_save, sender=exelUser)
def send_user_to_google_sheet(sender, instance, created, **kwargs):
    if created:
        append_data_to_sheet(
            instance.id,
            instance.name,
            getattr(instance, 'age', ''),
            instance.email,
            instance.phone
        )