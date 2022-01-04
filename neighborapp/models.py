from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    occupants = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def create_neigborhood(self):
        self.save()

    
class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=300,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50,null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)




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
    

class Business(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True, null=True)
    neighbourhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # create business
    def create_business(self):
        self.save()

    def __str__(self):
        return self.name