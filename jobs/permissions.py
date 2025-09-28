from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Admin users can do anything
    - Regular users can only read (GET, HEAD, OPTIONS)
    """
    def has_permission(self, request, view):
        # SAFE methods are always allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Only staff/admins can modify data
        return request.user and request.user.is_authenticated and request.user.is_staff
