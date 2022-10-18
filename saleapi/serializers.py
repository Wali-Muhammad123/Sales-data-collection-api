from rest_framework import serializers
from saleapi.models import Sale_data
class SaleSerializer(serializers.Serializer):
    class Meta:
        model=Sale_data
        fields=['id','date','time','customer_name','customer_address','customer_zipcode','customer_phone','customer_email','screenshot','status']
