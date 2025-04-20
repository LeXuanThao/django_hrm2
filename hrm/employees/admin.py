from django.contrib import admin
from .models import Account, Employee

admin.site.site_header = "HRM Admin"
admin.site.site_title = "HRM Admin Portal"
admin.site.index_title = "Welcome to HRM Admin Portal"

@admin.register(Account)
class AdminAccount(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at')
    search_fields = ('email',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets=(
        (None, { 'fields': ('email', 'password', 'avatar', 'is_active', 'is_staff', 'is_superuser') }),
    )

@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display = ('id', 'account___email', 'fullname', 'birth_day', 'hire_date', 'termination_date')
    search_fields = ('first_name', 'last_name', 'account__email')
    list_filter = ('hire_date', 'termination_date')
    ordering = ('-hire_date',)
    list_per_page = 20
    list_select_related = ('account',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('account')

    def account___email(self, obj):
        return obj.account.email if obj.account else None
    account___email.short_description = 'Account'
    