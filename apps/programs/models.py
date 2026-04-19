from django.db import models

# ==========================================================
# Program Categories
# ==========================================================
CATEGORY_CHOICES = [
    ("pre_primary", "Pre-Primary School"),
    ("learning_hub", "Ramakrishna Learning Hub"),
    ("health_awareness", "Health Camps & Awareness"),
    ("organic_plantation", "Organic / Plantation Initiatives"),
    ("cultural_events", "Cultural / National Events"),
]

# ==========================================================
# Program Model
# ==========================================================
class Program(models.Model):
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='programs/', blank=True, null=True)

    # Additional info for reporting / display
    total_beneficiaries = models.PositiveIntegerField(blank=True, null=True)
    volunteers_count = models.PositiveIntegerField(blank=True, null=True)
    sponsors = models.TextField(
        blank=True, null=True,
        help_text="List supporting organizations separated by commas or new lines"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Program"
        verbose_name_plural = "Programs"

    def __str__(self):
        category_display = self.get_category_display() if self.category else "No Category"
        return f"{self.title} ({category_display})"