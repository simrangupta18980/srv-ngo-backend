from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    EnvironmentActivityListAPIView,
    EnvironmentActivityViewSet,
)

# ==========================================================
# ROUTER FOR ADMIN CRUD
# ==========================================================
router = DefaultRouter()
router.register(r'environment', EnvironmentActivityViewSet, basename='environment')

# ==========================================================
# URL PATTERNS
# ==========================================================
urlpatterns = [

    # ------------------------------------------------------
    # PUBLIC READ-ONLY ENDPOINT
    # Example: /api/environment/
    # ------------------------------------------------------
    path(
        "",
        EnvironmentActivityListAPIView.as_view(),
        name="environment-list",
    ),

    # ------------------------------------------------------
    # ADMIN FULL CRUD ENDPOINTS
    # Example:
    #   GET     /api/environment/
    #   POST    /api/environment/
    #   PUT     /api/environment/<id>/
    #   DELETE  /api/environment/<id>/
    # ------------------------------------------------------
    path("", include(router.urls)),
]