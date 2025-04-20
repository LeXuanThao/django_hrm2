from django.contrib import admin
from .models import SpecialDate, WorkType, WorkSchedule, EmployeeWorkTime, AttendanceLog

@admin.register(SpecialDate)
class SpecialDateAdmin(admin.ModelAdmin):
    list_display = ('date', 'is_holiday', 'description')
    search_fields = ('description',)
    list_filter = ('is_holiday',)
    ordering = ('date',)
    date_hierarchy = 'date'
    list_per_page = 20

@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ('work_type', 'day_of_week', 'start_time', 'end_time', 'break_start_time', 'break_end_time')
    search_fields = ('work_type__name',)
    list_filter = ('work_type', 'day_of_week')
    ordering = ('work_type', 'day_of_week')

class WorkScheduleInline(admin.TabularInline):
    model = WorkSchedule
    extra = 1
    fields = ('day_of_week', 'start_time', 'end_time', 'break_start_time', 'break_end_time')
    ordering = ('day_of_week',)

@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [WorkScheduleInline]

@admin.register(EmployeeWorkTime)
class EmployeeWorkTimeAdmin(admin.ModelAdmin):
    list_display = ('employee', 'work_type', 'start_date', 'end_date')
    search_fields = ('employee__first_name', 'employee__last_name', 'work_type__name')
    list_filter = ('work_type',)
    ordering = ('employee', 'start_date')
    date_hierarchy = 'start_date'
    list_per_page = 20

@admin.register(AttendanceLog)
class AttendanceLogAdmin(admin.ModelAdmin):
    list_display = ('employee', 'check_in_time', 'check_out_time', 'work_schedule', 'special_date')
    search_fields = ('employee__first_name', 'employee__last_name')
    list_filter = ('work_schedule',)
    ordering = ('-check_in_time',)
    date_hierarchy = 'check_in_time'
    list_per_page = 20