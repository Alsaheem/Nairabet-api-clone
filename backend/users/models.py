from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# The user profile model
class Profile(models.Model):
    # The user profile model
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # To check if this user is an addicted playr like TOBEZ OR GABRAIEL
    #  OR OLUMIDE BELLO ADDICTION TO BREAST...OR MY ADDICTION TO ASS
    is_addicted = models.BooleanField(default=False)
    # The current ammount that the user has in his account
    current_ammount = models.IntegerField()
    profile_image = models.FileField(blank=True, null=True)


# this is to create a user profile  instance immediately a user is created
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=kwargs.get('instance'))