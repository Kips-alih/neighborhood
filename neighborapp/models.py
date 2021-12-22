from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.name

class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=300,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location=models.CharField(max_length=50,null=True)



    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
    

    def update_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    

