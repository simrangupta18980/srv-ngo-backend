from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgramListAPIView, ProgramViewSet


# ==========================================================
# DRF ROUTER FOR ADMIN CRUD
# ==========================================================
router = DefaultRouter()
router.register(r"", ProgramViewSet, basename="program")


# ==========================================================
# URL PATTERNS
# ==========================================================
urlpatterns = [

    # ------------------------------------------------------
    # PUBLIC READ-ONLY API
    # Example:
    #   GET /api/programs/list/
    # ------------------------------------------------------
    path(
        "list/",
        ProgramListAPIView.as_view(),
        name="program-list",
    ),

    # ------------------------------------------------------
    # ADMIN FULL CRUD API
    # Example:
    #   GET     /api/programs/
    #   POST    /api/programs/
    #   PUT     /api/programs/<id>/
    #   DELETE  /api/programs/<id>/
    # ------------------------------------------------------
    path("", include(router.urls)),
]