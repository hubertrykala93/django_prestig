from shop.models import DeliveryDetails
from rest_framework import serializers


class DeliveryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryDetails
        exclude = ["uuid"]
