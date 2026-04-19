from rest_framework import serializers
from .models import EnvironmentActivity, EnvironmentActivityImage


class EnvironmentActivityImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = EnvironmentActivityImage
        fields = ("id", "image", "uploaded_at")

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class EnvironmentActivitySerializer(serializers.ModelSerializer):
    images = EnvironmentActivityImageSerializer(many=True, read_only=True)

    class Meta:
        model = EnvironmentActivity
        fields = (
            "id",
            "title",
            "description",
            "date",
            "location",
            "objective",
            "total_beneficiaries",
            "supporting_organization",
            "created_at",
            "images",
        )
