from rest_framework.permissions import BasePermission


class LabelPermission(BasePermission):
    def has_permission(self, request, view):
        if request.action in ['list']:
            return True

    def has_object_permission(self, request, view, obj):
        return obj.to_user == request.user.id
