from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import ContactMessage, Contact
from .serializers import ContactMessageSerializer, ContactSerializer


# ==========================================================
# CONTACT MESSAGE APIs (FORM SUBMISSIONS)
# ==========================================================

class ContactMessageListAPIView(ListAPIView):
    """
    GET:
    List all contact messages.

    Can be restricted to admin users later if required.
    """

    queryset = ContactMessage.objects.all().order_by("-created_at")
    serializer_class = ContactMessageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ContactMessageCreateAPIView(CreateAPIView):
    """
    POST:
    Create a new contact message from the frontend contact form.
    """

    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ContactMessageViewSet(viewsets.ModelViewSet):
    """
    Admin Full CRUD for Contact Messages

    Features:
    - View all messages
    - Update messages (mark as read / resolved)
    - Delete messages
    """

    queryset = ContactMessage.objects.all().order_by("-created_at")
    serializer_class = ContactMessageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ==========================================================
# ORGANIZATION CONTACT DETAILS APIs
# ==========================================================

class ContactViewSet(viewsets.ModelViewSet):
    """
    Admin CRUD for Organization Contact Details

    Allows:
    - Add address
    - Update phone/email
    - Update Google map location
    - Delete contact information
    """

    queryset = Contact.objects.all().order_by("-created_at")
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]