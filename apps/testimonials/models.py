from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Testimonial(models.Model):

    # ======================================================
    # BASIC INFORMATION
    # ======================================================
    name = models.CharField(
        max_length=200,
        help_text="Name of the person giving the testimonial"
    )

    # designation instead of role (frontend me same name use karna hoga)
    designation = models.CharField(
        max_length=200,
        blank=True,
        help_text="Designation or role of the person"
    )

    message = models.TextField(
        help_text="Testimonial message or feedback"
    )

    # ======================================================
    # PHOTO
    # ======================================================
    photo = models.ImageField(
        upload_to="testimonials/",
        blank=True,
        null=True,
        help_text="Optional photo of the person"
    )

    # ======================================================
    # RELATED PROGRAM (OPTIONAL)
    # ======================================================
    program = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional: Program name related to this testimonial"
    )

    # ======================================================
    # RATING (1 to 5)
    # ======================================================
    rating = models.IntegerField(
        default=5,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        help_text="Rating given by the person (1 to 5)"
    )

    # ======================================================
    # DISPLAY SETTINGS
    # ======================================================
    featured = models.BooleanField(
        default=False,
        help_text="Mark this testimonial as featured"
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Uncheck to hide testimonial from website"
    )

    # ======================================================
    # CREATED TIME
    # ======================================================
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # ======================================================
    # META OPTIONS
    # ======================================================
    class Meta:
        ordering = ["-featured", "-created_at"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    # ======================================================
    # STRING REPRESENTATION
    # ======================================================
    def __str__(self):
        return f"{self.name} ({self.designation})" if self.designation else self.name