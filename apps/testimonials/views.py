from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Testimonial
from .serializers import TestimonialSerializer


# ==========================================================
# PUBLIC LIST API (ALREADY EXISTING – NOT REMOVED)
# ==========================================================
class TestimonialListView(generics.ListAPIView):
    """
    Public endpoint:
    - Shows only active testimonials
    - Featured testimonials first
    - Latest testimonials next
    """

    serializer_class = TestimonialSerializer

    def get_queryset(self):
        return (
            Testimonial.objects
            .filter(is_active=True)
            .order_by("-featured", "-created_at")
        )

    def get_serializer_context(self):
        """
        Pass request object to serializer
        so that absolute image URLs can be generated.
        """
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


# ==========================================================
# ADMIN CRUD VIEWSET (PROFESSIONAL STRUCTURE)
# ==========================================================
class TestimonialViewSet(viewsets.ModelViewSet):
    """
    Admin CRUD:
    - Create testimonial
    - Update testimonial
    - Delete testimonial
    - Activate / Deactivate testimonial
    """

    queryset = Testimonial.objects.all().order_by("-created_at")
    serializer_class = TestimonialSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        """
        Ensure serializer also receives request
        when used in admin CRUD operations.
        """
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context