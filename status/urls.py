from django.urls import path
from .views import loads, update

urlpatterns = [
    path('status', loads),  # api: server/status
    path('update', update)  # api: server/update
]
