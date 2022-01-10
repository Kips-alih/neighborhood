from django.test import TestCase
from django.contrib.auth.models import User
from .models import  Profile,Neighborhood,Post,Business,Location


# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(username="test_user")
        self.profile = Profile(name="user",email="user@gmail.com",profile_pic="",bio="Test Profile_pic",user=user,location="Nairobi",neighborhood="hood")

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_update_profile(self):
        self.profile.update_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Test Location')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.location.save_location()
        self.location.delete()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)