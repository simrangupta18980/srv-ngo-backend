from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TestimonialListView, TestimonialViewSet


# ==========================================================
# ROUTER FOR ADMIN CRUD OPERATIONS
# ==========================================================
router = DefaultRouter()

router.register(
    r"admin",
    TestimonialViewSet,
    basename="testimonial-admin"
)


# ==========================================================
# URL PATTERNS
# ==========================================================
urlpatterns = [

    # ------------------------------------------------------
    # PUBLIC TESTIMONIAL LIST API
    #
    # Example:
    #   GET /api/testimonials/
    # ------------------------------------------------------
    path(
        "",
        TestimonialListView.as_view(),
        name="testimonials-list"
    ),

    # ------------------------------------------------------
    # ADMIN CRUD ROUTES
    #
    # Examples:
    #   GET     /api/testimonials/admin/
    #   POST    /api/testimonials/admin/
    #   PUT     /api/testimonials/admin/{id}/
    #   DELETE  /api/testimonials/admin/{id}/
    # ------------------------------------------------------
    path(
        "",
        include(router.urls)
    ),
]