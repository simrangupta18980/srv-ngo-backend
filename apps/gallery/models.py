from django.db import models

class GalleryImage(models.Model):
    # ✅ Gallery Categories (Admin dropdown me dikhega)
    CATEGORY_CHOICES = [
        ("education", "Education Program"),
        ("health", "Health Camp"),
        ("environment", "Environment / Plantation"),
        ("events", "Events & Celebration"),
        ("general", "General Activities"),
    ]

    # Title of photo
    title = models.CharField(max_length=200)

    # Short description (optional)
    description = models.TextField(blank=True, null=True)  # ✅ Optional now

    # Image upload folder → media/gallery/
    image = models.ImageField(upload_to="gallery/")

    # Category dropdown
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="general"
    )

    # Auto timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
