from django.urls import path
from .views import auto_complete, history_check

urlpatterns = [
    path('company/name', auto_complete),  # api: compute/company/name
    path('company/price/history', history_check)  # api: compute/company/price/history
]
