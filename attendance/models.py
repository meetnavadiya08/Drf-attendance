from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendance")
    date = models.DateField(auto_now_add=True)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=(("Present", "Present"), ("Absent", "Absent"), ("On Leave", "On Leave")),
        default="Present"
    )

    def __str__(self):
        return f"{self.employee.name} - {self.date} ({self.status})"
