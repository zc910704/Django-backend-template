from django.urls import path
from .views import loads

urlpatterns = [
    path('status', loads)  # api: server/status
]
