from rest_framework import serializers
from .models import GalleryImage


class GalleryImageSerializer(serializers.ModelSerializer):
    # Image URL full path ke saath frontend me jayega
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = GalleryImage
        fields = "__all__"
