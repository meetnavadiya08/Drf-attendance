from django.contrib import admin
from .models import Employee, Attendance

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'is_active', 'created_at')
    search_fields = ('full_name', 'email')
    list_filter = ('is_active',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'date', 'check_in', 'check_out', 'status', 'created_at')
    list_filter = ('status', 'date')
    search_fields = ('employee__full_name', 'employee__email')
