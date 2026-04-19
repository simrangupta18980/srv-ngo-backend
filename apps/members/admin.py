from django.contrib import admin
from django.utils.html import format_html
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    """
    Admin configuration for NGO Members / Leadership
    """

    # =========================
    # Columns shown in admin list page
    # =========================
    list_display = (
        'photo_preview',
        'name',
        'designation',
        'email',
        'phone',
        'is_leadership',
        'display_order',
        'created_at',
    )

    # Make order editable directly in list page
    list_editable = (
        'display_order',
        'is_leadership',
    )

    # Sidebar filters
    list_filter = (
        'designation',
        'is_leadership',
        'created_at',
    )

    # Search capability
    search_fields = (
        'name',
        'designation',
        'email',
    )

    # Readonly fields
    readonly_fields = (
        'created_at',
        'updated_at',
        'photo_preview',
    )

    # Default ordering in admin panel
    ordering = (
        '-is_leadership',
        'display_order',
        'name',
    )

    # Admin form layout
    fieldsets = (

        ("Basic Information", {
            "fields": (
                "name",
                "designation",
                "photo",
                "photo_preview",
            )
        }),

        ("Profile Information", {
            "fields": (
                "bio",
                "message",
            )
        }),

        ("Contact Details", {
            "fields": (
                "email",
                "phone",
            )
        }),

        ("Leadership Settings", {
            "fields": (
                "is_leadership",
                "display_order",
            )
        }),

        ("System Information", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),

    )

    # =========================
    # Photo preview in admin
    # =========================
    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;border-radius:50%;object-fit:cover;" />',
                obj.photo.url
            )
        return "No Image"

    photo_preview.short_description = "Photo"