from django.db import models


# ==========================================================
# CONTACT FORM MESSAGES (USER SUBMISSIONS)
# ==========================================================
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    # Optional fields (professional contact forms usually include these)
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=255, blank=True)

    message = models.TextField()

    # Admin management fields
    is_read = models.BooleanField(default=False)
    is_resolved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.email}"


# ==========================================================
# ORGANIZATION CONTACT DETAILS (STATIC INFO)
# ==========================================================
class Contact(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    # Google Maps location link
    map_link = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Detail"
        verbose_name_plural = "Contact Details"

    def __str__(self):
        return self.email