from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Job, Category, Company
from .serializers import JobSerializer, CategorySerializer, CompanySerializer
from .permissions import IsAdminOrReadOnly  # Double Check if file exists

# -------------------------------
# Category API
# -------------------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]  # Admins full access, users read-only
    lookup_field = 'slug'


# -------------------------------
# Company API
# -------------------------------
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminOrReadOnly]  # Admins full access, users read-only


# -------------------------------
# Job API
# -------------------------------
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.select_related('category', 'company', 'posted_by').all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Anyone can view, only logged-in users can create
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields users can filter/search/order by
    filterset_fields = ['location', 'job_type', 'category__slug', 'company__id']
    search_fields = ['title', 'location', 'company__name', 'category__name']
    ordering_fields = ['posted_at', 'title', 'location']

    def perform_create(self, serializer):
        # Save the user who posted the job
        serializer.save(posted_by=self.request.user)
