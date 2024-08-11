from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from shop.models import DeliveryDetails
from .serializers import DeliveryDetailsSerializer


class DeliveryDetailsDetailsAPIView(RetrieveAPIView):
    def get_queryset(self):
        return DeliveryDetails.objects.all()

    def get_serializer_class(self):
        return DeliveryDetailsSerializer

    def get(self, request, *args, **kwargs):
        try:
            delivery_details = self.get_object()
            serializer = self.get_serializer(delivery_details)

            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK,
            )

        except DeliveryDetails.DoesNotExist:
            return Response(
                data={
                    "error": f"Delivery Details with ID {self.kwargs.get('pk')} does not exist.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                data={
                    "error": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
