from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.contrib.auth import views 
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('neighborapp.urls')),
    path('accounts/register/', RegistrationView.as_view(success_url='/'),name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_then_login, name='logout'), 
]
