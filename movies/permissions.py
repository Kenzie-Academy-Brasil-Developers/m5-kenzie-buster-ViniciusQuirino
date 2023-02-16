from rest_framework import permissions


class IsEmployee(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(request.user.is_employee)
