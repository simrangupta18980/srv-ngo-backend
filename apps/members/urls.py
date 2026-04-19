from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    MemberListAPIView,
    LeadershipListAPIView,
    MemberViewSet
)

# ==========================================================
# ROUTER FOR ADMIN CRUD
# ==========================================================
router = DefaultRouter()
router.register(
    r'admin',
    MemberViewSet,
    basename='members-admin'
)

# ==========================================================
# URL PATTERNS
# ==========================================================
urlpatterns = [

    # ------------------------------------------------------
    # PUBLIC MEMBERS LIST
    # Example:
    #   GET /api/members/
    # ------------------------------------------------------
    path(
        "",
        MemberListAPIView.as_view(),
        name="member-list",
    ),

    # ------------------------------------------------------
    # LEADERSHIP MEMBERS (CEO / Founder / Board)
    # Example:
    #   GET /api/members/leadership/
    # ------------------------------------------------------
    path(
        "leadership/",
        LeadershipListAPIView.as_view(),
        name="members-leadership",
    ),

    # ------------------------------------------------------
    # ADMIN CRUD ENDPOINTS
    #
    # Example:
    #   GET     /api/members/admin/
    #   POST    /api/members/admin/
    #   PUT     /api/members/admin/<id>/
    #   DELETE  /api/members/admin/<id>/
    # ------------------------------------------------------
    path(
        "admin/",
        include(router.urls),
    ),
]