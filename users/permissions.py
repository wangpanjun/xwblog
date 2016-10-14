from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['create', 'metadata']:
            return True
        else:
            return request.user.is_authenticated()
