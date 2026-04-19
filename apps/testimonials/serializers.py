from rest_framework import serializers
from .models import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):

    # Full image URL for frontend usage
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        fields = "__all__"

    def get_photo_url(self, obj):
        """
        Returns absolute URL of the testimonial photo
        so React frontend can display it correctly.
        """
        request = self.context.get("request")

        if obj.photo:
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url

        return None