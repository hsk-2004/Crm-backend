"""
Central API URL configuration.
All app routers are combined here under a single 'api/' prefix
so that DRF router-generated URLs (including custom @action endpoints)
are all reachable.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from leads.views import LeadViewSet
from clients.views import ClientViewSet

router = DefaultRouter()
router.register(r'leads', LeadViewSet, basename='lead')
router.register(r'clients', ClientViewSet, basename='client')

urlpatterns = [
    # JWT auth endpoints (from users app)
    path('', include('users.urls')),
    # All ViewSet endpoints
    path('', include(router.urls)),
]
