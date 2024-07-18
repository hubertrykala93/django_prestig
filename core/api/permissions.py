from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, \
    CreateAPIView


class CustomNewsletterPermission(BasePermission):
    def has_permission(self, request, view):
        if isinstance(view, ListAPIView):
            return True

        if isinstance(view, RetrieveAPIView):
            return True

        if request.user and request.user.is_staff:
            return True

        if isinstance(view, CreateAPIView):
            raise PermissionDenied(
                detail="To perform this action, you must be an administrator.",
            )

        if request.user and request.user.is_authenticated:
            if isinstance(view, (RetrieveUpdateAPIView, RetrieveDestroyAPIView)):
                return True

        return False

    def has_object_permission(self, request, view, obj):
        if isinstance(view, RetrieveAPIView):
            return True

        if request.user and request.user.is_staff:
            return True

        if request.user and request.user.is_authenticated:
            if isinstance(view, (RetrieveUpdateAPIView, RetrieveDestroyAPIView)):
                if obj.email == request.user.email:
                    return obj.email == request.user.email
                else:
                    raise PermissionDenied(
                        detail="To perform this action, you need to be the owner of this object or an administrator.",
                    )

        return False
