from django.contrib import admin
from .models import HealthProgram, HealthProgramImage


# ✅ Inline for Multiple Images
class HealthProgramImageInline(admin.TabularInline):
    model = HealthProgramImage
    extra = 3  # Admin me default 3 image fields dikhenge
    fields = ("image",)


@admin.register(HealthProgram)
class HealthProgramAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "date",
        "location",
        "total_beneficiaries",
    )

    search_fields = (
        "title",
        "location",
        "guests",
    )

    list_filter = ("date",)

    ordering = ("-date",)

    fieldsets = (
        ("Basic Information", {
            "fields": (
                "title",
                "description",
                "objective",
            )
        }),
        ("Event Details", {
            "fields": (
                "date",
                "location",
                "total_beneficiaries",
            )
        }),
        ("Guests Information", {
            "fields": (
                "guests",
            )
        }),
    )

    # ✅ Multiple Images Inline Added
    inlines = [HealthProgramImageInline]


# (Optional but Recommended)
@admin.register(HealthProgramImage)
class HealthProgramImageAdmin(admin.ModelAdmin):
    list_display = ("program", "image")
