from django.urls import path, include
from . import views

urlpatterns = [
    path('main/', views.main),
    path('privacy/', views.privacy),
    path('service/', views.service),
]
