from django.db import models


class AttendanceRecord(models.Model):
    employee = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        related_name="attendance_records",
    )
    date = models.DateField()
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    notes = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ("employee", "date")
        ordering = ["-date", "-check_in"]

    def __str__(self) -> str:
        return f"{self.employee} - {self.date}"

    @property
    def worked_seconds(self) -> int:
        if self.check_in and self.check_out and self.check_out > self.check_in:
            return int((self.check_out - self.check_in).total_seconds())
        return 0
