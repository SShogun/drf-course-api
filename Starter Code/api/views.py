from django.shortcuts import get_object_or_404
from api.serializers import *
from api.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])  #converts django view to DRF view
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data) #Response is a DRF class that converts data to JSON or other formats

@api_view(['GET'])  
def product_detail(request, pk):
    products = get_object_or_404(Product, pk = pk)
    serializer = ProductSerializer(products)
    return Response(serializer.data)

@api_view(['GET'])  
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True) #since it an array of objects we use many=True
    return Response(serializer.data) 
