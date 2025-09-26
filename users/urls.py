from django.urls import path
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
]
