from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    # Columns visible in admin list page
    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "subject",
        "is_read",
        "is_resolved",
        "created_at",
    )

    # Search functionality
    search_fields = (
        "name",
        "email",
        "phone",
        "subject",
        "message",
    )

    # Filters on right side
    list_filter = (
        "is_read",
        "is_resolved",
        "created_at",
    )

    # Default ordering
    ordering = (
        "-created_at",
    )

    # Read-only fields
    readonly_fields = (
        "created_at",
    )

    # Admin form layout
    fieldsets = (
        ("User Information", {
            "fields": (
                "name",
                "email",
                "phone",
                "subject",
            )
        }),

        ("Message", {
            "fields": (
                "message",
            )
        }),

        ("Status", {
            "fields": (
                "is_read",
                "is_resolved",
            )
        }),

        ("System Information", {
            "fields": (
                "created_at",
            )
        }),
    )