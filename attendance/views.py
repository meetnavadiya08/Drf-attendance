from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import AttendanceRecord
from .serializers import AttendanceRecordSerializer


class AttendanceRecordViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.select_related("employee").all()
    serializer_class = AttendanceRecordSerializer

    # @action(detail=False, methods=["get"], url_path="health")
    # def health(self, request):
    #     return Response({"status": "ok", "time": timezone.now().isoformat()})

    @action(detail=False, methods=["post"], url_path="clock-in")
    def clock_in(self, request):
        """Clock in an employee for a date. Creates the record if missing.

        Request body:
        - employee or employee_id (int)
        - date (YYYY-MM-DD, optional; defaults to today)
        """
        employee_id = request.data.get("employee_id") or request.data.get("employee")
        if not employee_id:
            return Response({"detail": "employee_id required"}, status=400)
        date_value = request.data.get("date")
        date_value = date_value or timezone.localdate()
        record, _ = AttendanceRecord.objects.get_or_create(
            employee_id=employee_id,
            date=date_value,
        )
        if not record.check_in:
            record.check_in = timezone.now()    
            record.save(update_fields=["check_in"])
        return Response(AttendanceRecordSerializer(record).data)

    @action(detail=False, methods=["post"], url_path="clock-out")
    def clock_out(self, request):
        """Clock out an employee for a date. Requires an existing record.

        Request body:
        - employee or employee_id (int)
        - date (YYYY-MM-DD, optional; defaults to today)
        """
        employee_id = request.data.get("employee_id") or request.data.get("employee")
        if not employee_id:
            return Response({"detail": "employee_id required"}, status=400)
        date_value = request.data.get("date") or timezone.localdate()
        try:
            record = AttendanceRecord.objects.get(
                employee_id=employee_id, date=date_value
            )
        except AttendanceRecord.DoesNotExist:
            return Response({"detail": "clock in first"}, status=400)
        if not record.check_out:
            record.check_out = timezone.now()
            record.save(update_fields=["check_out"])
        return Response(AttendanceRecordSerializer(record).data)
