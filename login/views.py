from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# auth
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
# Extend_user
from . import models
# JSON
import json
# Create your views here.
response_dict = {}
token_dict = {}
data_dict = {}

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        if username:
            password = request.POST.get('password')
        else:
            # 当前端以payload形式发送JSON时，无法从POST方法取到值时，反序列化json
            request_payload_obj = json.loads(request.body)
            username = request_payload_obj['username']
            password = request_payload_obj['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            response_dict["code"] = 20000
            token_dict["token"] = username
            response_dict["data"] = token_dict
            print(response_dict)
            return JsonResponse(response_dict)
        else:
            response_dict["code"] = 50008
            token_dict["token"] = username
            response_dict["data"] = token_dict
            print(response_dict)
            return JsonResponse(response_dict)


def getInfo(request):
    if request:
        username = request.GET.get('token')
        user = User.objects.get(username=username)
        if user:
            data_dict = {}
            response_dict = {}
            ext_user = models.Extend_User.objects.get(user=user)

            response_dict["code"] = 20000

            data_dict['name'] = ext_user.real_name
            data_dict['avatar'] = ext_user.avatar
            data_dict['roles'] = ['admin']
            response_dict["data"] = data_dict
            response = JsonResponse(response_dict,json_dumps_params={'ensure_ascii':False})#事实上不加也可以
            return response


def user_logout(request):
  logout(request)
  response_dict = {}
  response_dict['code']= 20000
  response_dict['data']= 'success'
  return JsonResponse(response_dict)



#https://www.cnblogs.com/wf-skylark/p/9317096.html
#ensure_ascii是false的时候，可以返回非ASCII码的值，否则就会被JSON转义。
#response对象
#JSON序列化str = json.dumps(j)
#https://docs.djangoproject.com/en/2.1/ref/request-response/

