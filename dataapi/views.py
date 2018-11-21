from django.shortcuts import render
from . import models
from django.http import JsonResponse
import json

# Create your views here.

def CallListInfo(request):
  if request.methods == "GET":
    call_list = models.CallList.objects.all()
    return JsonResponse({'code': 20000, 'data': call_list})
  else:
    return JsonResponse({'code': 20001})

def DetailInfo(request):
  if request.method == "POST":
        callname = request.POST.get('callname')
        if callname:
          pass
        else:
          request_payload_obj = json.loads(request.body)
          callname = request_payload_obj['callname']
        try:
          call = CallList.objects.get(callname= callname)
          bidder = models.BidDetail.objects.filter(callfor = call)
          return JsonResponse({'code': 20000, 'data': bidder})
        except:
          return JsonResponse({'code': 20000, 'data': []})
