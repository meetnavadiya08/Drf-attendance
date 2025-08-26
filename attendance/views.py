from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import AttendanceRecord
from .serializers import AttendanceRecordSerializer


class AttendanceRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AttendanceRecord.objects.select_related("employee").all()
    serializer_class = AttendanceRecordSerializer

    @action(detail=False, methods=["post"], url_path="clock-in")
    def clock_in(self, request):
        employee_id = request.data.get("employee_id")
        if not employee_id:
            return Response({"detail": "employee_id required"}, status=400)
        record, _ = AttendanceRecord.objects.get_or_create(
            employee_id=employee_id,
            date=timezone.localdate(),
        )
        if not record.check_in:
            record.check_in = timezone.now()
            record.save(update_fields=["check_in"])
        return Response(AttendanceRecordSerializer(record).data)

    @action(detail=False, methods=["post"], url_path="clock-out")
    def clock_out(self, request):
        employee_id = request.data.get("employee_id")
        if not employee_id:
            return Response({"detail": "employee_id required"}, status=400)
        try:
            record = AttendanceRecord.objects.get(
                employee_id=employee_id, date=timezone.localdate()
            )
        except AttendanceRecord.DoesNotExist:
            return Response({"detail": "clock in first"}, status=400)
        if not record.check_out:
            record.check_out = timezone.now()
            record.save(update_fields=["check_out"])
        return Response(AttendanceRecordSerializer(record).data)
