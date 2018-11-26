from django.http import request, JsonResponse
from . import models
import json
# Create your views here.


def price_detail_info(request: request):
    """
    return the detail price of contract items that user search for
    """
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        if not keyword:
            keyword = json.loads(request.body)['keyword']
        query_set = models.ContractPrice.objects.filter(item__contains=keyword).values()
        return JsonResponse({'code': 20000, 'data': list(query_set)})
