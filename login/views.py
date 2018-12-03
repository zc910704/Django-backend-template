
from django.http import JsonResponse
# auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Extend_user
from . import models
# JSON
import json
# Create your views here.


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        if username:
            password = request.POST.get('password')
        else:  # 当前端以payload形式发送JSON时，无法从POST方法取到值时，反序列化JSON
            request_payload_obj = json.loads(request.body)
            username = request_payload_obj['username']
            password = request_payload_obj['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'code': 20000, 'data': {'token': username}})
        else:
            return JsonResponse({'code': 20001, 'message': '密码错误'})
    return JsonResponse({'code': 404})


def getInfo(request):
    if request:
        username = request.GET.get('token')
        user = User.objects.get(username=username)
        if user:
            ext_user = models.Extend_User.objects.get(user=user)
            return JsonResponse({'code': 20000,
                                 'data': {'name': ext_user.real_name,
                                          'avatar': ext_user.avatar,
                                          'roles': ['admin']}},
                                json_dumps_params={'ensure_ascii': False})  # 事实上不加也可以
        else:
            return JsonResponse({'code': 50014})


def user_logout(request):
    logout(request)
    return JsonResponse({'code': 20000, 'data': 'success'})

# https://www.cnblogs.com/wf-skylark/p/9317096.html
# ensure_ascii是false的时候，可以返回非ASCII码的值，否则就会被JSON转义。
# JSON序列化str = json.dumps(j) 参见：https://docs.djangoproject.com/en/2.1/ref/request-response/
