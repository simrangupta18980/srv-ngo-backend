from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    """
    Serializer for NGO Members / Leadership
    Used for API responses in frontend (React / Website)
    """

    class Meta:
        model = Member

        # All required fields for frontend display
        fields = [
            "id",
            "name",
            "designation",
            "photo",
            "bio",
            "message",
            "email",
            "phone",
            "is_leadership",
            "display_order",
            "created_at",
            "updated_at",
        ]

        # System fields should not be editable via API
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]