from rest_framework import serializers
from .models import Program

class ProgramSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(
        source='get_category_display',
        read_only=True
    )

    class Meta:
        model = Program
        fields = [
            'id',
            'title',
            'description',
            'category',
            'category_display',
            'location',
            'image',
            'date',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
