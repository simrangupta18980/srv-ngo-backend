from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404

from .models import Report
from .serializers import ReportSerializer

import os


# ==========================================================
# PUBLIC REPORT LIST API (READ-ONLY)
# ==========================================================
class ReportListAPIView(APIView):
    """
    Public Read-Only API
    --------------------
    - Lists all reports
    - Latest reports first
    """

    def get(self, request):
        reports = Report.objects.all().order_by("-created_at")
        serializer = ReportSerializer(
            reports,
            many=True,
            context={"request": request},  # Important for file URL
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


# ==========================================================
# FORCE DOWNLOAD VIEW (PUBLIC)
# ==========================================================
def download_report(request, pk):
    """
    Force file download by ID
    Example:
        GET /api/reports/download/5/
    """

    report = get_object_or_404(Report, pk=pk)

    if not report.file:
        raise Http404("File not found")

    file_path = report.file.path

    if not os.path.exists(file_path):
        raise Http404("File does not exist")

    return FileResponse(
        open(file_path, "rb"),
        as_attachment=True,
        filename=os.path.basename(file_path),
    )


# ==========================================================
# ADMIN FULL CRUD API
# ==========================================================
class ReportViewSet(viewsets.ModelViewSet):
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

    queryset = Report.objects.all().order_by("-created_at")
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        """
        Required for proper file URL handling
        """
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def perform_create(self, serializer):
        """
        Extend later if you want created_by field
        """
        serializer.save()