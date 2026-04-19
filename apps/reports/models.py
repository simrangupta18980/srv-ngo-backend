from django.db import models


class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ("annual", "Annual Report"),
        ("audit", "Audit Report"),
    ]

    title = models.CharField(max_length=255)

    report_type = models.CharField(
        max_length=20,
        choices=REPORT_TYPE_CHOICES
    )

    year = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="reports/")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.get_report_type_display()})"
