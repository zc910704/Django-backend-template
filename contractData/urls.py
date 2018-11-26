from django.urls import path
from .views import price_detail_info

urlpatterns = [
    path('price/detail', price_detail_info)  # api: contract/price/detail
]
