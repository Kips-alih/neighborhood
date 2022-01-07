from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.name

class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    image = CloudinaryField('image',null=True)
    description= models.TextField(max_length=300,null=True)
    occupants = models.IntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def create_neigborhood(self):
        self.save()

    @classmethod
    def delete_neighborhood(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_neighborhood(cls, id):
        cls.objects.filter(id=id).update()

    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood

    @classmethod
    def find_neigborhood(cls, id):
        hood = cls.objects.get(id=id)
        return hood

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=300,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE,null=True)



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
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # create business
    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.update()

    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    def __str__(self):
        return self.name

#Post model
class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='hood_post')
    created_at = models.DateTimeField(auto_now_add=True)

    def create_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self):
        self.update()

    def __str__(self):
        return self.title
