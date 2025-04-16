from rest_framework import permissions

class CustomPermissions(permissions.BasePermission):
    """
    Custom permission to allow staff to POST, and users to edit their own records.
    """

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.is_staff:
            return True
        # For methods other than POST, allow if user is authenticated
        return request.user.is_authenticated
