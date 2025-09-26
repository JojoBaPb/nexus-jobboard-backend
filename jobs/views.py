from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job, Category, Company
from .serializers import JobSerializer, CategorySerializer, CompanySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]  # Only admin can CRUD categories
    lookup_field = 'slug'

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUser]  # Only admin can CRUD companies

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.select_related('category', 'company', 'posted_by').all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['location', 'job_type', 'category__slug', 'company__id']

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)
