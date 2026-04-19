from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Program
from .serializers import ProgramSerializer


# ==========================================================
# PUBLIC READ-ONLY API
# ==========================================================
class ProgramListAPIView(ListAPIView):
    """
    Public Read-Only API
    --------------------
    - Anyone can view program list
    - Latest programs appear first
    - No create/update/delete allowed here
    """
    serializer_class = ProgramSerializer

    def get_queryset(self):
        return Program.objects.all().order_by("-created_at")


# ==========================================================
# ADMIN FULL CRUD API
# ==========================================================
class ProgramViewSet(viewsets.ModelViewSet):
    """
    Admin CRUD API
    --------------
    Public Users:
        - Can only READ (GET)

    Authenticated Admin:
        - Can CREATE
        - Can UPDATE
        - Can DELETE
    """

    queryset = Program.objects.all().order_by("-created_at")
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Optional: If in future you want to track who created it
        """
        serializer.save()