from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

from .models import NGOProfile, OrganizationDetails
from .serializers import NGOProfileSerializer, OrganizationDetailsSerializer


# ======================================================
# SIMPLE LANDING PAGE (TEST PAGE FOR ROOT URL)
# ======================================================
def home(request):
    """
    Simple HTML landing page used only for testing
    whether Django server is running properly.
    """
    return HttpResponse("""
    <html>
    <head>
        <title>SRV NGO</title>
    </head>
    <body style="font-family: Arial; text-align:center; margin-top:100px;">
        <h1>Welcome to SRV NGO!</h1>
        <p>This is the landing page for your NGO project.</p>
    </body>
    </html>
    """)


# ======================================================
# NGO PROFILE API (LIST)
# ======================================================
class NGOProfileListAPIView(ListAPIView):
    """
    Returns NGO profiles as a LIST.

    Even if only one record exists, the frontend
    will safely receive an array.
    """

    queryset = NGOProfile.objects.all()
    serializer_class = NGOProfileSerializer


# ======================================================
# NGO PROFILE API (ALIAS FOR FRONTEND)
# ======================================================
class NGOListAliasView(APIView):
    """
    This view provides a compatibility endpoint
    for frontend routes like:

    /api/core/ngo/

    It internally returns the same data as
    NGOProfileListAPIView but through APIView.
    """

    def get(self, request):

        profiles = NGOProfile.objects.all()

        serializer = NGOProfileSerializer(
            profiles,
            many=True
        )

        return Response(serializer.data)


# ======================================================
# NGO PROFILE API (SINGLE RECORD CRUD)
# ======================================================
class NGOProfileView(APIView):
    """
    Handles single NGO profile operations.

    GET     -> Return single NGO profile
    POST    -> Create NGO profile
    PUT     -> Update existing NGO profile
    DELETE  -> Delete NGO profile
    """

    def get(self, request):

        profile = NGOProfile.objects.first()

        if not profile:
            return Response(
                {"message": "NGO profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = NGOProfileSerializer(profile)

        return Response(serializer.data)

    def post(self, request):

        serializer = NGOProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request):

        profile = NGOProfile.objects.first()

        if not profile:
            return Response(
                {"message": "NGO profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = NGOProfileSerializer(
            profile,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request):

        profile = NGOProfile.objects.first()

        if not profile:
            return Response(
                {"message": "NGO profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        profile.delete()

        return Response(
            {"message": "NGO profile deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )


# ======================================================
# ORGANIZATION DETAILS API
# ======================================================
class OrganizationDetailsView(APIView):
    """
    Returns only the active OrganizationDetails record.

    This endpoint is used for the
    'Organization Transparency' section in the frontend.
    """

    def get(self, request):

        details = OrganizationDetails.objects.filter(
            is_active=True
        ).first()

        if not details:
            return Response(
                {"message": "No active organization details found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = OrganizationDetailsSerializer(details)

        return Response(serializer.data)