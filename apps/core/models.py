from django.db import models


class NGOProfile(models.Model):
    """
    Main NGO Profile Information
    Basic Information + About + Transparency
    """

    # 🔹 Basic Information
    name = models.CharField(
        max_length=255,
        default="Shri Ramakrishna Vivekananda Jnana Vikasa Shikshana Samste"
    )
    short_name = models.CharField(max_length=100, blank=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    map_link = models.URLField(blank=True)

    # 🔹 Branding
    logo = models.ImageField(upload_to="ngo/logo/", blank=True, null=True)

    # 🔹 About Section
    about = models.TextField()
    vision = models.TextField()
    mission = models.TextField()
    objectives = models.TextField()

    # 🔹 Transparency Information
    registration_number = models.CharField(max_length=200, blank=True)
    established_date = models.CharField(max_length=100, blank=True)
    legal_identity = models.CharField(max_length=200, blank=True)
    governing_body_details = models.TextField(blank=True)
    registered_location = models.CharField(max_length=200, blank=True)

    # 🔹 Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "NGO Profile"
        verbose_name_plural = "NGO Profiles"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class OrganizationDetails(models.Model):
    """
    Detailed Transparency / Organization Information
    """

    registration_number = models.CharField(max_length=100)

    established_date = models.DateField()

    legal_identity = models.TextField()

    registered_location = models.CharField(max_length=200)

    office_address = models.TextField()

    mobile_number_1 = models.CharField(max_length=15)

    mobile_number_2 = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    mobile_number_3 = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Organization Detail"
        verbose_name_plural = "Organization Details"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.registration_number} - {self.registered_location}"