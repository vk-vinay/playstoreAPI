from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,serializers

import json
from api.core import Scraper


@api_view(['GET'])
def search(request, format=None):
    key= request.query_params['q']
    print(key)
    apps=Scraper.get_search(str(key))
    return Response(,status=status.HTTP_200_OK)

@api_view(['GET'])
def details(request, format=None):
    return Response(" details is workin")