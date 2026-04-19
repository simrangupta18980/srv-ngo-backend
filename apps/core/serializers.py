from rest_framework import serializers

from .models import NGOProfile, OrganizationDetails


# ======================================================
# NGO PROFILE SERIALIZER
# ======================================================
class NGOProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for NGOProfile model.

    Handles NGO basic information such as:
    - NGO name
    - About section
    - Mission
    - Vision
    - Objectives
    - Other NGO related metadata
    """

    class Meta:
        model = NGOProfile
        fields = "__all__"
        read_only_fields = ["created_at"]


# ======================================================
# ORGANIZATION DETAILS SERIALIZER
# ======================================================
class OrganizationDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer for OrganizationDetails model.

    Used for the 'Organization Transparency' section
    on the frontend website.
    """

    class Meta:
        model = OrganizationDetails
        fields = "__all__"
        read_only_fields = ["created_at"]


# ======================================================
# NGO SERIALIZER (FRONTEND COMPATIBILITY)
# ======================================================
class NGOSerializer(serializers.ModelSerializer):
    """
    Compatibility serializer.

    Some frontend implementations expect
    a serializer named 'NGOSerializer'.

    This serializer maps to NGOProfile model
    to prevent breaking existing APIs.
    """

    class Meta:
        model = NGOProfile
        fields = "__all__"