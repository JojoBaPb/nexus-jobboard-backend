from rest_framework.routers import DefaultRouter
from .views import JobViewSet, CategoryViewSet, CompanyViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'companies', CompanyViewSet, basename='company')

urlpatterns = router.urls
