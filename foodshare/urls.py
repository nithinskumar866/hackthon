from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('donate/', views.donate, name='donate'),
    path('map/', views.map_view, name='map'),
    path('tracking/', views.tracking, name='tracking'),
    path('notifications/', views.notifications, name='notifications'),
    path('register-ngo/', views.register_ngo, name='register_ngo'),
    path('registration-success/', views.registration_success, name='registration_success'),
]