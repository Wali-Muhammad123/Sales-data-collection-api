from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from saleapi.models import Sale_data
from saleapi.serializers import SaleSerializer
# Create your views here.
class SaleAPI(APIView):
    def get(self,request):
        sale=Sale_data.objects.all()
        serializer=SaleSerializer(sale,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



