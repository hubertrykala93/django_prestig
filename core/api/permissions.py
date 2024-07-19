from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, \
    RetrieveDestroyAPIView


class NewsletterCustomPermission(BasePermission):
    def has_permission(self, request, view):
        if isinstance(view, (ListAPIView, RetrieveAPIView)):
            return True

        if isinstance(view, CreateAPIView):
            if request.user.is_authenticated and request.user.is_staff:
                return True

            else:
                raise PermissionDenied(
                    detail="To perform this action, you must be an administrator.",
                )

        if isinstance(view, (RetrieveUpdateAPIView, RetrieveDestroyAPIView)):
            if request.user.is_authenticated or request.user.is_staff:
                return True

            else:
                raise PermissionDenied(
                    detail="To perform this action, you need to be the owner of this object or an administrator.",
                )

        raise PermissionDenied(
            detail="To perform this action, you must be an administrator.",
        )

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_staff:
            return True

        if request.user.is_authenticated:
            if obj.email == request.user.email:
                return True

            else:
                raise PermissionDenied(
                    detail="To perform this action, you need to be the owner of this object or an administrator."
                )

        raise PermissionDenied(
            detail="To perform this action, you need to be the owner of this object or an administrator.",
        )
