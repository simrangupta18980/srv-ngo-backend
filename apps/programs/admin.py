from django.contrib import admin
from .models import Program

# ==========================================================
# Program Admin Registration
# ==========================================================
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    # Display important fields in the admin list view
    list_display = (
        "title",
        "category",
        "date",
        "location",
        "total_beneficiaries",
        "volunteers_count",
    )

    # Enable filtering by category and date
    list_filter = (
        "category",
        "date",
    )

    # Enable search for title, description, and location
    search_fields = (
        "title",
        "description",
        "location",
    )

    # Make timestamp fields read-only
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    # Order newest programs first by date
    ordering = ("-date",)