from rest_framework.routers import DefaultRouter

from .views import SitesViewSet

router = DefaultRouter()

router.register(r'', SitesViewSet, basename='sites')

urlpatterns = router.urls
