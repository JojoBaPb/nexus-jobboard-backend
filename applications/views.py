from rest_framework import viewsets, permissions
from .models import Application
from .serializers import ApplicationSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        - Admins see all applications
        - Regular users only see their own
        """
        user = self.request.user
        if user.is_staff:
            return Application.objects.select_related("job", "applicant", "job__company", "job__category").all()
        return Application.objects.select_related("job", "applicant", "job__company", "job__category").filter(applicant=user)

    def perform_create(self, serializer):
        """
        - Applicant is automatically set to the logged-in user
        """
        serializer.save(applicant=self.request.user)

