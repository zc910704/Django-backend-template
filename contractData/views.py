from django.http import JsonResponse
from .models import ContractPrice
import json
# Create your views here.


def price_detail_info(request):
    """
    return the detail price of contract items that user search for
    """
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        if not keyword:
            keyword = json.loads(request.body)['keyword']
        query_set = ContractPrice.objects.filter(item__contains=keyword) \
            .values('contract__contractName', 'contract__contractDate', 'item', 'feature', 'description',
                    'unit', 'priceNet', 'priceTaxed', 'comment')
        return JsonResponse({'code': 20000, 'data': list(query_set)})
