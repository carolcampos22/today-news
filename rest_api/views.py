from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from base.models import Register
from rest_api.serializers import NewsModelSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello World!, {request.data.get("name")}'})
    return Response({'message': f'Hello World!'})

class NewsModelViewset(ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = NewsModelSerializer


