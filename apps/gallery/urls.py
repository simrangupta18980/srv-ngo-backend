from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GalleryListAPIView, GalleryImageViewSet

# ==========================================================
# ROUTER FOR ADMIN CRUD
# ==========================================================
router = DefaultRouter()
router.register(r"admin", GalleryImageViewSet, basename="gallery-admin")

# ==========================================================
# URL PATTERNS
# ==========================================================
urlpatterns = [

    # ------------------------------------------------------
    # PUBLIC LIST (EXISTING – NOT REMOVED)
    # Example:
    #   GET /api/gallery/
    #   GET /api/gallery/?category=health
    # ------------------------------------------------------
    path("", GalleryListAPIView.as_view(), name="gallery-list"),

    # ------------------------------------------------------
    # ADMIN CRUD ROUTES
    # Example:
    #   GET     /api/gallery/admin/
    #   POST    /api/gallery/admin/
    #   PUT     /api/gallery/admin/5/
    #   DELETE  /api/gallery/admin/5/
    # ------------------------------------------------------
    path("", include(router.urls)),
]