from django.urls import path

from .views import (
    NGOProfileListAPIView,
    NGOProfileView,
    OrganizationDetailsView
)

urlpatterns = [

    # ======================================
    # NGO PROFILE LIST API
    # ======================================
    # Example:
    # http://127.0.0.1:8000/api/core/
    path(
        "",
        NGOProfileListAPIView.as_view(),
        name="ngo-profile-list"
    ),

    # ======================================
    # NGO PROFILE LIST (ALIAS FOR FRONTEND)
    # ======================================
    # Example:
    # http://127.0.0.1:8000/api/core/ngo/
    path(
        "ngo/",
        NGOProfileListAPIView.as_view(),
        name="ngo-profile-list-alias"
    ),

    # ======================================
    # SINGLE NGO PROFILE API
    # ======================================
    # Example:
    # http://127.0.0.1:8000/api/core/profile/
    path(
        "profile/",
        NGOProfileView.as_view(),
        name="ngo-profile"
    ),

    # ======================================
    # ORGANIZATION DETAILS API
    # ======================================
    # Example:
    # http://127.0.0.1:8000/api/core/organization/
    path(
        "organization/",
        OrganizationDetailsView.as_view(),
        name="organization-details"
    ),

]