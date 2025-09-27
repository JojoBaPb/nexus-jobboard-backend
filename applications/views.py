from rest_framework import viewsets, permissions
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Admins see all applications.
        Users only see their own.
        Swagger (fake view) and anonymous get empty queryset.
        """
        # Swagger / schema generation
        if getattr(self, "swagger_fake_view", False):
            return Application.objects.none()

        user = self.request.user
        if not user.is_authenticated:
            return Application.objects.none()

        if user.is_staff:
            return Application.objects.all()
        return Application.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
