from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="avatars/")

    def __str__(self):
        return f"{self.user.username}"

@receiver(post_save, sender = User)
def create_profile_from_user(sender, instance, created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
