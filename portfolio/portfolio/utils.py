from pymongo import MongoClient
from django.conf import settings

def get_db_handle():
    client = MongoClient(
        host = settings.MONGO_DB['HOST'],
        port = int(settings.MONGO_DB['PORT'])
    )
    return client