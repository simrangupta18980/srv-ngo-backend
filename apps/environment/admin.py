from django.contrib import admin
from .models import EnvironmentActivity, EnvironmentActivityImage


# 🔥 Inline model for multiple photos
class EnvironmentActivityImageInline(admin.TabularInline):
    model = EnvironmentActivityImage
    extra = 3  # Default empty image upload fields
    fields = ("image", "uploaded_at")
    readonly_fields = ("uploaded_at",)


# 🔥 Main Activity Admin
@admin.register(EnvironmentActivity)
class EnvironmentActivityAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "location")
    search_fields = ("title", "location")
    list_filter = ("date",)
    inlines = [EnvironmentActivityImageInline]

    fieldsets = (
        ("Basic Information", {
            "fields": ("title", "date", "location")
        }),
        ("Activity Details", {
            "fields": ("objective", "description", "total_beneficiaries", "supporting_organization")
        }),
    )


# 🔥 Separate Image Admin (Optional but good for management)
@admin.register(EnvironmentActivityImage)
class EnvironmentActivityImageAdmin(admin.ModelAdmin):
    list_display = ("activity", "uploaded_at")
    list_filter = ("uploaded_at",)
