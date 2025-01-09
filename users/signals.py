# signal is sent when object is saved
from django.db.models.signals import post_save
# post_save signal sender
from django.contrib.auth.models import User
# signal receiver is a function that performs task: automatically make profile for each new user with default img 
from django.dispatch import receiver
# import the model
from .models import Profile

# function to create new profiles with decorator
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs): 
  if created: 
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): 
    instance.profile.save() 


