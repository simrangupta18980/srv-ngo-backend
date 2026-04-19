from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import GalleryImage
from .serializers import GalleryImageSerializer


# ==========================================================
# PUBLIC GALLERY LIST API
# ==========================================================
class GalleryListAPIView(ListAPIView):
    """
    Public Read-Only API
    --------------------
    - Lists all gallery images
    - Supports category filtering
    - Latest images appear first
    """

    serializer_class = GalleryImageSerializer

    def get_queryset(self):
        queryset = GalleryImage.objects.all().order_by("-created_at")

        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category=category)

        return queryset

    def get_serializer_context(self):
        """
        Required for proper ImageField absolute URLs
        """
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


# ==========================================================
# ADMIN FULL CRUD API
# ==========================================================
class GalleryImageViewSet(viewsets.ModelViewSet):
    """
    Admin CRUD API
    --------------
    Public Users:
        - Can READ only

    Authenticated Admin:
        - Can CREATE
        - Can UPDATE
        - Can DELETE
    """

    queryset = GalleryImage.objects.all().order_by("-created_at")
    serializer_class = GalleryImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        """
        Ensures proper image URL generation in admin responses
        """
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def perform_create(self, serializer):
        """
        Extend later if you want created_by field
        """
        serializer.save()