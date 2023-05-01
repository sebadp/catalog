from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminProductPermission(BasePermission):
    """
    Custom permission class to allow only admin users to create/update/delete products
    """

    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_superuser
