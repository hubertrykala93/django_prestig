from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from shop.models import Product


class AddToWishlistAPIView(APIView):
    def post(self, request, *args, **kwargs):
        product_id = request.data.get("id", None)

        if product_id == "":
            return Response(
                data={
                    "error": "Product does not exists.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if product_id is None:
            return Response(
                data={
                    "error": "Product does not exists.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if product_id is not None:
            try:
                product = Product.objects.get(id=product_id)

            except Product.DoesNotExist:
                return Response(
                    data={
                        "error": "Product does not exists.",
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

            request.user.profile.wishlist.add(product)

            if not request.session.get("wishlist"):
                request.session["wishlist"] = []

            if product_id not in request.session["wishlist"]:
                request.session["wishlist"].append(int(product_id))
                request.session.modified = True

            return Response(
                data={
                    "success": f"The product '{product.name}' has been added to your favorites list.",
                },
                status=status.HTTP_200_OK,
            )
