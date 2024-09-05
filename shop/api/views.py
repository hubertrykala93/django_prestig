from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from shop.models import Product


class AddToWishlistAPIView(APIView):
    def post(self, request, *args, **kwargs):
        product_id = request.data.get("id", None)

        if not product_id:
            return Response(
                data={
                    "error": "Product does not exists.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            product = Product.objects.get(id=product_id)

        except Product.DoesNotExist:
            return Response(
                data={
                    "error": "Product does not exists.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        if product not in request.user.profile.wishlist.all():
            request.user.profile.wishlist.add(product)

            return Response(
                data={
                    "success": f"The product '{product.name}' has been added to your favorites list.",
                },
                status=status.HTTP_200_OK,
            )

        else:
            request.user.profile.wishlist.remove(product)

            return Response(
                data={
                    "success": f"The product '{product.name}' has been removed from your favorites list.",
                },
                status=status.HTTP_200_OK,
            )
