from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Admin users can do anything
    - Regular users can only read (GET, HEAD, OPTIONS)
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff  # Only admin can POST, PUT, PATCH, DELETE
