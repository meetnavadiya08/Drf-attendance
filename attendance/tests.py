from django.test import TestCase
from django.utils import timezone
from employees.models import Employee
from .models import AttendanceRecord


class AttendanceModelTests(TestCase):
    def test_worked_seconds_calculation(self):
        employee = Employee.objects.create(first_name="A", last_name="B", email="a@example.com")
        now = timezone.now()
        record = AttendanceRecord.objects.create(
            employee=employee,
            date=timezone.localdate(),
            check_in=now,
            check_out=now + timezone.timedelta(hours=1),
        )
        self.assertEqual(record.worked_seconds, 3600)

# Create your tests here.
