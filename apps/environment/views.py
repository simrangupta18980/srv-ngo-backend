from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import EnvironmentActivity
from .serializers import EnvironmentActivitySerializer


# ==========================================================
# PUBLIC READ-ONLY API
# ==========================================================
class EnvironmentActivityListAPIView(ListAPIView):
    """
    Public Read-Only API
    --------------------
    - Anyone can view environment activities
    - Ordered by latest date first
    - No create/update/delete allowed here
    """

    queryset = EnvironmentActivity.objects.all().order_by("-date")
    serializer_class = EnvironmentActivitySerializer

    def get_serializer_context(self):
        """
        Required for image/file URL generation
        """
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


# ==========================================================
# ADMIN FULL CRUD API
# ==========================================================
class EnvironmentActivityViewSet(viewsets.ModelViewSet):
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

    queryset = EnvironmentActivity.objects.all().order_by("-date")
    serializer_class = EnvironmentActivitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        """
        Ensures proper media URL handling in admin too
        """
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def perform_create(self, serializer):
        """
        Optional future extension:
        Save creator if needed
        """
        serializer.save()