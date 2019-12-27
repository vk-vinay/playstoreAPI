from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def search(request, format=None):
    return Response("search is workin")

@api_view(['GET'])
def details(request, format=None):
    return Response(" details is workin")