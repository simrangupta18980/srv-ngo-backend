from rest_framework import serializers
from .models import ContactMessage, Contact


# ==========================================================
# CONTACT FORM MESSAGE SERIALIZER
# ==========================================================
class ContactMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for user-submitted contact messages.
    Handles validation and API data conversion.
    """

    class Meta:
        model = ContactMessage
        fields = "__all__"
        read_only_fields = ("created_at",)

    # Optional validation (professional improvement)
    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Name must contain at least 2 characters.")
        return value


# ==========================================================
# ORGANIZATION CONTACT DETAILS SERIALIZER
# ==========================================================
class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for organization contact details.
    Used for address, phone, email, and map location.
    """

    class Meta:
        model = Contact
        fields = "__all__"
        read_only_fields = ("created_at",)