from django.http import JsonResponse
from dataapi.models import CallList, BidDetail
import json


# Create your views here.


def auto_complete(request):
    """

    :param request:
    :return: JSON, the auto_complete result of company name which is input now
    """
    if request.method == 'POST':
        company = request.POST.get('company')
        if not company:
            company = json.loads(request.body)['company']
        print(company)
        if company:
            query_set = BidDetail.objects.filter(biddername__contains=company).values('biddername').distinct()
            return JsonResponse({'code': 20000, 'data': list(query_set)})
        else:
            return JsonResponse({'code': 20000, 'data': None})
    return JsonResponse({'code': 20000, 'data': None})


def history_check(request):
    """
    :param request:
    :return: the result of company bid history by JSON
    """
    if request.method == 'POST':
        company = request.POST.get('company')
        if not company:
            company = json.loads(request.body)['company']
        print(company)
        if company:
            query_set = BidDetail.objects.filter(biddername=company).values('bidderprice',
                                                                            'callfor__calldate', 'callfor__callname',
                                                                            'callfor__calllimit', 'callfor__winner',
                                                                            'callfor__method')
            print(query_set)
            return JsonResponse({'code': 20000, 'data': list(query_set)})
