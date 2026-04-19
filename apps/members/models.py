from django.db import models


class Member(models.Model):
    """
    NGO Board Members / Team Members / Leadership
    Used for displaying NGO team members, board members,
    and leadership messages such as CEO / Founder.
    """

    # =========================
    # DESIGNATION CHOICES
    # =========================
    DESIGNATION_CHOICES = [
        ("president", "President"),
        ("vice_president", "Vice President"),
        ("secretary", "Secretary"),
        ("vice_secretary", "Vice Secretary"),
        ("treasurer", "Treasurer"),
        ("member", "Member"),
        ("ceo", "CEO"),
        ("volunteer", "Volunteer"),
        ("donor", "Donor"),
    ]

    # =========================
    # BASIC INFORMATION
    # =========================
    name = models.CharField(max_length=200)

    designation = models.CharField(
        max_length=50,
        choices=DESIGNATION_CHOICES,
        help_text="Select the role of the member in the NGO"
    )

    # =========================
    # MEDIA
    # =========================
    photo = models.ImageField(upload_to="members/")

    # =========================
    # PROFILE INFORMATION
    # =========================
    bio = models.TextField(
        blank=True,
        null=True,
        help_text="Short biography of the member"
    )

    # =========================
    # LEADERSHIP MESSAGE
    # =========================
    message = models.TextField(
        blank=True,
        null=True,
        help_text="Leadership message such as CEO or Founder message"
    )

    # =========================
    # CONTACT INFORMATION
    # =========================
    email = models.EmailField(blank=True, null=True)

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    # =========================
    # LEADERSHIP FLAG
    # =========================
    is_leadership = models.BooleanField(
        default=False,
        help_text="Enable this for CEO / Founder / Leadership members"
    )

    # =========================
    # DISPLAY ORDER
    # =========================
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Controls the order of members on the website (lower number appears first)"
    )

    # =========================
    # TIMESTAMPS
    # =========================
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    # =========================
    # MODEL META
    # =========================
    class Meta:

        ordering = ["-is_leadership", "display_order", "id"]

        verbose_name = "Member"

        verbose_name_plural = "Members"

    # =========================
    # STRING REPRESENTATION
    # =========================
    def __str__(self):
        return f"{self.name} - {self.get_designation_display()}"