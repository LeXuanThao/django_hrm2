from django.contrib import admin
from .models import Department, Position, JobTitle, EmployeeInOrganization

@admin.register(Department)
class AdminDepartment(admin.ModelAdmin):
    list_display = ('name', 'parent', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 20
    ordering = ('created_at',)
    list_filter = ('created_at',)

@admin.register(Position)
class AdminPosition(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('name', 'description')}),
    )
    list_per_page = 20
    ordering = ('created_at',)
    list_filter = ('created_at',)
    list_select_related = ('department',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('department')
    
@admin.register(JobTitle)
class AdminJobTitle(admin.ModelAdmin):
    list_display = ('name', 'department', 'position', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('name', 'description', 'department', 'position')}),
    )
    list_per_page = 20
    ordering = ('created_at',)
    list_filter = ('department', 'position')
    list_select_related = ('department', 'position')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('department', 'position')
    
@admin.register(EmployeeInOrganization)
class AdminEmployeeInOrganization(admin.ModelAdmin):
    list_display = ('employee', 'department', 'position', 'job_title', 'start_date', 'end_date')
    search_fields = ('employee__first_name', 'employee__last_name', 'department__name', 'position__name', 'job_title__name')
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 20
    ordering = ('created_at',)
    list_filter = ('department', 'position', 'job_title')
    list_select_related = ('employee', 'department', 'position', 'job_title')