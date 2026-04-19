from django.contrib import admin
from django.utils.html import format_html
from .models import Testimonial


# =========================
# ADMIN PANEL TITLE
# =========================
admin.site.site_header = "SRV NGO Admin Panel"
admin.site.site_title = "SRV NGO Admin"
admin.site.index_title = "Welcome to SRV NGO Dashboard"


# =========================
# TESTIMONIAL ADMIN
# =========================
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "designation",
        "rating",
        "featured",
        "is_active",
        "image_preview",
        "created_at",
    )

    list_editable = (
        "featured",
        "rating",
        "is_active",
    )

    list_filter = (
        "featured",
        "is_active",
        "rating",
    )

    search_fields = (
        "name",
        "designation",
        "program",
    )

    readonly_fields = (
        "image_preview",
    )

    # =========================
    # IMAGE PREVIEW IN ADMIN
    # =========================
    def image_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:50%; object-fit:cover;" />',
                obj.photo.url
            )
        return "No Image"

    image_preview.short_description = "Photo Preview"