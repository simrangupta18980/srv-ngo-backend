from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Member
from .serializers import MemberSerializer


# ==========================================================
# PUBLIC READ-ONLY API
# ==========================================================
class MemberListAPIView(ListAPIView):
    """
    Public Read-Only API
    --------------------
    Lists all NGO Members / Volunteers / Team members

    Ordering logic:
    1. Leadership members first
    2. Then by display_order
    3. Then by ID (stable ordering)
    """

    queryset = Member.objects.all().order_by(
        "-is_leadership",
        "display_order",
        "id"
    )

    serializer_class = MemberSerializer


# ==========================================================
# LEADERSHIP API (CEO / Founder / Board)
# ==========================================================
class LeadershipListAPIView(ListAPIView):
    """
    Public API for Leadership Members

    Used for:
    - CEO Message
    - Founder Message
    - Board Members

    Filters members where is_leadership=True
    """

    queryset = Member.objects.filter(
        is_leadership=True
    ).order_by(
        "display_order",
        "id"
    )

    serializer_class = MemberSerializer


# ==========================================================
# ADMIN FULL CRUD API
# ==========================================================
class MemberViewSet(viewsets.ModelViewSet):
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

    queryset = Member.objects.all().order_by(
        "-is_leadership",
        "display_order",
        "id"
    )

    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        """
        Required when using ImageField / FileField
        to generate absolute media URLs
        """
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def perform_create(self, serializer):
        """
        Optional extension:
        Can attach logged-in user as creator later
        """
        serializer.save()