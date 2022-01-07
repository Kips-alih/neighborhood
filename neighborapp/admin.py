from django.contrib import admin
from neighborapp.models import Post, Profile,Neighborhood,Location,Category,Business

# Register your models here.
admin.site.register(Profile)
admin.site.register(Neighborhood)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Business)
admin.site.register(Post)



