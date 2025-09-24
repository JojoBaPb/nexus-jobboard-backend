from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Swagger / ReDoc schema configuration
schema_view = get_schema_view(
   openapi.Info(
      title="Nexus Jobboard API",
      default_version='v1',
      description="API documentation for Nexus Jobboard backend",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="support@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # App endpoints
    path('api/users/', include('users.urls')),          # User registration, profile, logout, password change
    path('api/jobs/', include('jobs.urls')),            # Job listings CRUD
    path('api/applications/', include('applications.urls')),  # Job applications CRUD

    # JWT authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
