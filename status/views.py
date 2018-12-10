from django.http import JsonResponse
from .models import RecentUpdate
import psutil


# Create your views here.


def loads(request):
    """
    :param request: request
    :return: JSON, the memory and cpu load status of the server
    """
    cpu_load = psutil.cpu_percent()
    memo_load = psutil.virtual_memory().percent
    django_user = str(request.user)
    return JsonResponse({'code': 20000,
                         'data': {'cpu_load': cpu_load,
                                  'memo_load': memo_load,
                                  'user': django_user}})


def update(request):
    """
    :param request: http request
    :return: the recent update list
    """
    if request.method == "GET":
        query_set = RecentUpdate.objects.all().values('id', 'time', 'title', 'content')
        return JsonResponse({'code': 20000, 'data': list(query_set)})
