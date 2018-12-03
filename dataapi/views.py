from . import models
from django.http import JsonResponse
import json

# Create your views here.

def callListInfo(request):
    if request.method == "GET":
        call_list = models.CallList.objects.all().values('status', 'callname', 'calldate', 'winner', 'method', 'calllimit')
        return JsonResponse({'code': 20000, 'data': list(call_list)})
    else:
        return JsonResponse({'code': 20001})


def detailInfo(request):
    """
    :param request:
    :return:
    """
    if request.method == "POST":
        callname = request.POST.get('callname')
        if callname:
            pass
        else:
            request_payload_obj = json.loads(request.body)
            callname = request_payload_obj['callname']
        try:
            call = models.CallList.objects.get(callname=callname)
            bidder = models.BidDetail.objects.filter(callfor=call)
            return JsonResponse({'code': 20000, 'data': bidder})
        except:
            return JsonResponse({'code': 20000, 'data': []})

def searchCallList(request):
    if request.method == "POST":
        search = request.POST.get('search')
        if search:
            pass
        else:
            request_payload_obj = json.loads(request.body)
            search = request_payload_obj['search']
        calllist = models.CallList.objects.all().values('status', 'callname', 'calldate', 'winner', 'method', 'calllimit')
        return JsonResponse({'code': 20000, 'data': list(calllist)})

def calldetailList(request):
    print(request.user)
    if request.method == "POST":
        call = request.POST.get('call')
        if call:
            pass
        else:
            request_payload_obj = json.loads(request.body)
            call = request_payload_obj['call']
        bidders = models.BidDetail.objects.filter(callfor__callname=call).values('biddername', 'bidderprice')
        return JsonResponse({'code': 20000, 'data': list(bidders)})
