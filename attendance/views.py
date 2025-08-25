from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer

from rest_framework import viewsets
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
