from django.http import JsonResponse
from .models import ContractPrice, BidPrice
import json
# Create your views here.
from django.contrib.auth.decorators import login_required


def price_detail_info(request):
    """
    return the detail price of contract items that user search for
    """
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        database_set = request.POST.get('database')
        if not keyword:
            keyword = json.loads(request.body)['keyword']
            database_set = json.loads(request.body)['database']
        print(keyword)
    if keyword:
        query_set_list = None
        if database_set == 0 or not database_set:
            # 0 means none database selected
            pass
        elif database_set == 1 or database_set - 3 == 1:
            # 1 means the Contract database selected
            query_set_list += ContractPrice.objects.filter(item__contains=keyword) \
                .values('contract__contractName', 'contract__contractDate', 'item',
                        'feature', 'description', 'unit', 'priceNet',
                        'priceTaxed', 'classify', 'comment')
        elif database_set == 3 or database_set - 1 == 3:
            # 3 means the Bid database selected
            query_set_list += BidPrice.objects.filter(item__contains=keyword) \
                .values('contract__contractName', 'contract__contractDate', 'item',
                        'feature', 'description', 'unit', 'priceNet',
                        'priceTaxed', 'classify', 'comment')
        if len(query_set_list) == 2:
            query_set = (query_set_list[0] | query_set_list[1]).distinct()
        else:
            query_set = query_set_list

        return JsonResponse({'code': 20000, 'data': list(query_set)})
