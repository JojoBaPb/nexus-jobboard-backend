from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Application
from .serializers import ApplicationSerializer
from .permissions import IsAdminOrOwner

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.select_related('job', 'applicant').all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['job', 'status', 'applicant']

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)
