from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from shop.models import DeliveryDetails
from .serializers import DeliveryDetailsSerializer
