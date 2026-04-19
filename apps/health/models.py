from django.db import models


class HealthProgram(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    objective = models.TextField(blank=True, null=True)

    date = models.DateField()
    location = models.CharField(max_length=200)
    total_beneficiaries = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    # Professional Guests Field
    guests = models.TextField(
        blank=True,
        null=True,
        help_text="Enter Chief Guest and other guests. Add each guest on a new line."
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title


# ✅ Model for Multiple Images
class HealthProgramImage(models.Model):
    program = models.ForeignKey(
        HealthProgram,
        on_delete=models.CASCADE,
        related_name="images"   # ✅ Important (Already Correct)
    )
    image = models.ImageField(upload_to="health/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.program.title} Image"