from django.contrib import admin
from .models import SabbaticalRequest, SabbaticalType, SabbaticalApproval, EmployeeSabbatical

class SabbaticalApprovalInline(admin.TabularInline):
    model = SabbaticalApproval
    extra = 1
    fields = ('approver', 'status', 'comments')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

@admin.register(SabbaticalRequest)
class AdminSabbaticalRequest(admin.ModelAdmin):
    list_display = ('employee', 'sabbatical_type', 'start_date', 'end_date', 'status', 'created_at')
    search_fields = ('employee__first_name', 'employee__last_name', 'sabbatical_type__name')
    list_filter = ('status',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 20
    inlines = [SabbaticalApprovalInline]

@admin.register(SabbaticalType)
class AdminSabbaticalType(admin.ModelAdmin):
    list_display = ('name', 'description', 'max_days', 'is_active', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('is_active',)
    ordering = ('name',)
    list_per_page = 20

@admin.register(EmployeeSabbatical)
class AdminEmployeeSabbatical(admin.ModelAdmin):
    list_display = ('employee', 'start_date', 'end_date', 'total', 'used', 'remaining', 'created_at')
    search_fields = ('employee__first_name', 'employee__last_name')
    list_filter = ('employee',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 20