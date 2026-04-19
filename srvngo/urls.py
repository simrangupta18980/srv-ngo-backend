from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

# JWT Authentication Views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# =====================================================
# ROOT API TEST ENDPOINT
# =====================================================
def api_home(request):
    """
    Root API endpoint used to verify that
    the Django backend server is running.
    """
    return JsonResponse({
        "status": "Django API Running",
        "project": "SRV NGO Backend"
    })


# =====================================================
# MAIN URL ROUTES
# =====================================================
urlpatterns = [

    # -------------------------------------------------
    # ROOT API TEST
    # -------------------------------------------------
    path(
        "",
        api_home,
        name="api-home"
    ),

    # -------------------------------------------------
    # DJANGO ADMIN PANEL
    # -------------------------------------------------
    path(
        "admin/",
        admin.site.urls
    ),

    # =================================================
    # JWT AUTHENTICATION ROUTES
    # =================================================
    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),

    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),

    # =================================================
    # CORE API (NGO PROFILE + ORGANIZATION)
    # =================================================
    path(
        "api/core/",
        include("apps.core.urls")
    ),

    # =================================================
    # NGO MAIN API (ALIAS FOR CORE)
    # =================================================
    path(
        "api/ngo/",
        include("apps.core.urls")
    ),

    # =================================================
    # PROGRAMS API
    # =================================================
    path(
        "api/programs/",
        include("apps.programs.urls")
    ),

    # =================================================
    # HEALTH PROGRAMS API
    # =================================================
    path(
        "api/health/",
        include("apps.health.urls")
    ),

    # =================================================
    # ENVIRONMENT ACTIVITIES API
    # =================================================
    path(
        "api/environment/",
        include("apps.environment.urls")
    ),

    # =================================================
    # GALLERY API
    # =================================================
    path(
        "api/gallery/",
        include("apps.gallery.urls")
    ),

    # =================================================
    # REPORTS API
    # =================================================
    path(
        "api/reports/",
        include("apps.reports.urls")
    ),

    # =================================================
    # MEMBERS API
    # =================================================
    path(
        "api/members/",
        include("apps.members.urls")
    ),

    # =================================================
    # TESTIMONIALS API
    # =================================================
    path(
        "api/testimonials/",
        include("apps.testimonials.urls")
    ),

    # =================================================
    # CONTACT API
    # =================================================
    path(
        "api/contact/",
        include("apps.contact.urls")
    ),
]


# =====================================================
# MEDIA FILES (SERVE MEDIA IN DEVELOPMENT)
# =====================================================
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )