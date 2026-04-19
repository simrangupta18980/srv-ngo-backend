# backend/reports/admin.py

from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'report_type', 'year', 'file', 'created_at')
    list_filter = ('report_type', 'year')
    search_fields = ('title', 'report_type', 'year', 'description')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
