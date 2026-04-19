from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ContactMessageCreateAPIView,
    ContactMessageListAPIView,
    ContactMessageViewSet,
    ContactViewSet,
)

# ==========================================================
# ROUTER FOR ADMIN CRUD (PROFESSIONAL SETUP)
# ==========================================================

router = DefaultRouter()

# Admin CRUD for contact messages
router.register(r"admin", ContactMessageViewSet, basename="contact-admin")

# Admin CRUD for organization contact details
router.register(r"details", ContactViewSet, basename="contact-details")


# ==========================================================
# URL PATTERNS
# ==========================================================

urlpatterns = [

    # ------------------------------------------------------
    # GET: List all contact messages
    # Example:
    #   GET /api/contact/
    # ------------------------------------------------------
    path(
        "",
        ContactMessageListAPIView.as_view(),
        name="contact-list"
    ),

    # ------------------------------------------------------
    # POST: Submit contact form
    # Example:
    #   POST /api/contact/send/
    # ------------------------------------------------------
    path(
        "send/",
        ContactMessageCreateAPIView.as_view(),
        name="contact-create"
    ),

    # ------------------------------------------------------
    # ADMIN CRUD ROUTES
    # Example:
    #   GET     /api/contact/admin/
    #   PUT     /api/contact/admin/5/
    #   DELETE  /api/contact/admin/5/
    # ------------------------------------------------------
    path(
        "",
        include(router.urls)
    ),
]