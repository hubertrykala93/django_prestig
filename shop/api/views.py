from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from shop.models import DeliveryDetails
from .serializers import DeliveryDetailsSerializer
from accounts.models import User, Profile


class DeliveryDetailsUpdateAPIView(UpdateAPIView):
    def get_object(self):
        return DeliveryDetails.objects.get(id=self.request.user.profile.delivery_details.id)

    def get_serializer_class(self):
        return DeliveryDetailsSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data, partial=True)

        if serializer.is_valid():
            self.perform_update(serializer=serializer)

            return Response(
                data={
                    "success": "Your delivery information has been successfully updated.",
                },
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                data=serializer.errors,
            )

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data, partial=True)

        if serializer.is_valid():
            self.perform_update(serializer=serializer)

            return Response(
                data={
                    "success": "Your delivery information has been successfully updated.",
                },
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                data=serializer.errors,
            )
