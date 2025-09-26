from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    """
    Admins have full access. Users can only view/create their own applications.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.applicant == request.user
