"""bid_system_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views as log
from dataapi import views as data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/login', log.user_login),
    path('user/info', log.getInfo),
    path('data/calllistinfo', data.callListInfo),
    path('user/logout', log.user_logout),
    path('data/detailinfo', data.detailInfo),
    path('data/search-call-list', data.searchCallList),
    path('data/call-detail-list', data.calldetailList)
]
