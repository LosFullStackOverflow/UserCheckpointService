from django.urls import path

from .services.checkpoint_service import checkpoint

urlpatterns = [
    path('checkpoint', checkpoint)
]

