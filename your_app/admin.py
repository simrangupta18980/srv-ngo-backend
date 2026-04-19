from django.contrib import admin


class CustomAdminSite(admin.AdminSite):

    class Media:
        css = {
            "all": ("admin/css/admin_custom.css",)
        }


admin.site.__class__ = CustomAdminSite