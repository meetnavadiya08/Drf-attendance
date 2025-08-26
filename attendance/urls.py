from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AttendanceRecordViewSet

router = DefaultRouter()
router.register(r"attendance", AttendanceRecordViewSet, basename="attendance")

urlpatterns = [
    path("api/", include(router.urls)),
]
    