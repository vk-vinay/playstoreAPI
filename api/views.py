from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,serializers
from api.models import app_deatils
from api.core import Scraper


@api_view(['GET'])
def search(request, format=None):
    key= request.query_params['q']
    print(key)
    apps=Scraper.get_search(str(key))
    return Response(apps,status=status.HTTP_200_OK)

@api_view(['GET'])
def details(request, format=None):
    app_id=request.query_params['id']
    #ob=app_deatils.objects.get(app_id=str(app_id))
    #print(ob)
    details=Scraper.get_details(str(app_id))
    print(app_id)
    if(details=='app not found use app id =com.example.xyz'):
        return Response(details,status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(details,status=status.HTTP_200_OK)