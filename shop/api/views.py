from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from shop.models import DeliveryDetails
from .serializers import DeliveryDetailsSerializer


class DeliveryDetailsUpdateAPIView(UpdateAPIView):
    def get_object(self):
        pass

    def get_serializer_class(self):
        return DeliveryDetailsSerializer

    def patch(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass
