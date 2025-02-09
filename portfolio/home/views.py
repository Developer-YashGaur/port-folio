from django.http import HttpResponse, JsonResponse
from portfolio.utils import get_db_handle

# Create your views here.
def index(request):
    client = get_db_handle()
    db_name = client['WordLinks']
    collection = db_name['MiMobiles']
    data = collection.find({}, {"_id":0, "price": 1})
    product_list = list(data)
    
    return JsonResponse({"products": product_list})