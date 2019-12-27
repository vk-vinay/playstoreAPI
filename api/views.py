from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,serializers
from api.models import app_db
from api.core import Scraper
import json
from django.core import serializers


@api_view(['GET'])
def search(request, format=None):
    key= request.query_params['q']
    print(key)
    apps=Scraper.get_search(str(key))
    return Response(apps,status=status.HTTP_200_OK)

@api_view(['GET'])
def details(request, format=None):
    app_id=request.query_params['id']

    dt=pull_data(app_id)
   # push_data(details,app_id)

    if(details=='app not found use app id =com.example.xyz'):
        return Response(dt['fields'],status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(dt,status=status.HTTP_200_OK)


def push_data(details,app_id):
    c = app_db(app_id=app_id, app_name=details[0], description=details[1], updated=details[2], size=details[3],
               installs=details[4], version=details[5], android=details[6]).save()

def pull_data(app_id):
    data=app_db.objects.filter(app_id=app_id)
    if(data.__len__()>0):
        return json.loads(serializers.serialize('json',data))
    else:
        details = Scraper.get_details(str(app_id))
        push_data(details,app_id)
        return details

