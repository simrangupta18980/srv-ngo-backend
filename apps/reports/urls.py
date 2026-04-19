from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ReportListAPIView,
    ReportViewSet,
    download_report,
)

# ==========================================================
# ROUTER FOR ADMIN CRUD
# ==========================================================
router = DefaultRouter()
router.register(r"admin", ReportViewSet, basename="reports-admin")


# ==========================================================
# URL PATTERNS
# ==========================================================
urlpatterns = [

    # ------------------------------------------------------
    # PUBLIC REPORT LIST API
    # Example:
    #   GET /api/reports/
    # ------------------------------------------------------
    path(
        "",
        ReportListAPIView.as_view(),
        name="report-list",
    ),

    # ------------------------------------------------------
    # FORCE DOWNLOAD API
    # Example:
    #   GET /api/reports/download/5/
    # ------------------------------------------------------
    path(
        "download/<int:pk>/",
        download_report,
        name="download-report",
    ),

    # ------------------------------------------------------
    # ADMIN FULL CRUD API
    # Example:
    #   GET     /api/reports/admin/
    #   POST    /api/reports/admin/
    #   PUT     /api/reports/admin/5/
    #   DELETE  /api/reports/admin/5/
    # ------------------------------------------------------
    path("", include(router.urls)),
]