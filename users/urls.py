from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegisterView,
    ProfileView,
    LogoutView,
    ChangePasswordView,
)

urlpatterns = [
    # User registration
    path('register/', RegisterView.as_view(), name='register'),

    # User profile (get/update)
    path('profile/', ProfileView.as_view(), name='profile'),

    # Logout (blacklist refresh token)
    path('logout/', LogoutView.as_view(), name='logout'),

    # Change password
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    # Login & Refresh endpoints
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
