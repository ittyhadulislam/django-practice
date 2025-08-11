from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactForm, name='contact'),
    path('success', views.success, name='success')
]