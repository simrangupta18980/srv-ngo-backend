from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import NGOProfile, OrganizationDetails


# =====================================
# ADMIN PANEL BRANDING
# =====================================

admin.site.site_header = "SRV NGO Admin Panel"
admin.site.site_title = "SRV NGO Admin"
admin.site.index_title = "Welcome to SRV NGO Dashboard"


# =====================================
# HIDE UNNECESSARY MODELS FROM CLIENT
# =====================================

admin.site.unregister(Group)
admin.site.unregister(User)


# =====================================
# NGO PROFILE ADMIN
# =====================================

@admin.register(NGOProfile)
class NGOProfileAdmin(admin.ModelAdmin):

    # Columns shown in admin list view
    list_display = (
        "id",
        "name",
        "short_name",
        "registration_number",
        "established_date",
        "legal_identity",
        "phone",
        "email",
        "created_at",
    )

    # Search support
    search_fields = (
        "name",
        "short_name",
        "registration_number",
        "legal_identity",
        "phone",
        "email",
    )

    # Read-only system fields
    readonly_fields = (
        "created_at",
    )

    # Latest profile first
    ordering = (
        "-created_at",
    )

    # Admin form grouping
    fieldsets = (

        # Basic NGO information
        ("Basic Information", {
            "fields": (
                "name",
                "short_name",
            )
        }),

        # Contact details including Google Maps location
        ("Contact Details", {
            "fields": (
                "address",
                "phone",
                "email",
                "map_link",   # Google Maps Location Link
            )
        }),

        # Registration and legal information
        ("Organization Details", {
            "fields": (
                "registration_number",
                "established_date",
                "legal_identity",
                "registered_location",
                "governing_body_details",
            )
        }),

        # Website content sections
        ("Content Section", {
            "fields": (
                "about",
                "vision",
                "mission",
                "objectives",
            )
        }),

        # System metadata
        ("System Info", {
            "fields": (
                "created_at",
            )
        }),
    )


# =====================================
# ORGANIZATION DETAILS ADMIN
# =====================================

@admin.register(OrganizationDetails)
class OrganizationDetailsAdmin(admin.ModelAdmin):

    list_display = (
        "registration_number",
        "registered_location",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "registration_number",
        "registered_location",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )

    fieldsets = (

        ("Registration Information", {
            "fields": (
                "registration_number",
                "established_date",
                "legal_identity",
                "registered_location",
            )
        }),

        ("Office Details", {
            "fields": (
                "office_address",
                "mobile_number_1",
                "mobile_number_2",
                "mobile_number_3",
            )
        }),

        ("Status", {
            "fields": (
                "is_active",
                "created_at",
            )
        }),
    )