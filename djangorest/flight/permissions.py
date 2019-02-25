from rest_framework.permissions import BasePermission
from .models import Flight


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Flight):
            return obj.user == request.user
        return obj.user == request.user