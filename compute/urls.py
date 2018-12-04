from django.urls import path
from .views import auto_complete

urlpatterns = [
    path('company/name', auto_complete)  # api: compute/company/name
]
