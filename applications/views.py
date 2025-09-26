from rest_framework import viewsets, permissions
from .models import Application
from .serializers import ApplicationSerializer

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission:
    - Admins can view all
    - Users can view their own applications only
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.applicant == request.user

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.select_related('job', 'applicant').all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:  # Admin sees all
            return Application.objects.all()
        return Application.objects.filter(applicant=user)

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)

