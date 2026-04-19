from django.db import models


class EnvironmentActivity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    # Professional Fields
    location = models.CharField(max_length=255, blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    total_beneficiaries = models.CharField(max_length=150, blank=True, null=True)
    supporting_organization = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class EnvironmentActivityImage(models.Model):
    activity = models.ForeignKey(
        EnvironmentActivity,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(
        upload_to="environment/",
        blank=True,
        null=True
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return f"Image for {self.activity.title}"
