from django.urls import path
from .views import HealthProgramListAPIView, HealthProgramDetailAPIView


urlpatterns = [
    # ✅ List All Health Programs
    path("", HealthProgramListAPIView.as_view(), name="health-list"),

    # ✅ Single Program Detail (with multiple images)
    path("<int:pk>/", HealthProgramDetailAPIView.as_view(), name="health-detail"),
]
