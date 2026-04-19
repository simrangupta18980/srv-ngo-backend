from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import HealthProgram
from .serializers import HealthProgramSerializer


# ✅ List API (All Programs)
class HealthProgramListAPIView(ListAPIView):
    queryset = HealthProgram.objects.all().order_by("-date")
    serializer_class = HealthProgramSerializer


# ✅ Detail API (Single Program with Images)
class HealthProgramDetailAPIView(RetrieveAPIView):
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer
    lookup_field = "pk"
