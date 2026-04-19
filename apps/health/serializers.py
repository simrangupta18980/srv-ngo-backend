from rest_framework import serializers
from .models import HealthProgram, HealthProgramImage


# ✅ Multiple Images Serializer
class HealthProgramImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgramImage
        fields = ["id", "image"]


# ✅ MAIN SERIALIZER (Name MUST be HealthProgramSerializer)
class HealthProgramSerializer(serializers.ModelSerializer):
    images = HealthProgramImageSerializer(many=True, read_only=True)

    class Meta:
        model = HealthProgram
        fields = [
            "id",
            "title",
            "description",
            "objective",
            "date",
            "location",
            "total_beneficiaries",
            "guests",
            "images",
        ]