from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('form/',views.forms, name = 'forms'),
    path('django_form/',views.django_form, name = 'django_form'),
    path('profile/',views.profile, name = 'profile')
]
