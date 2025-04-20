from django.db import models

class EmployeeSabbatical(models.Model):
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total = models.FloatField(default=0.0)
    used = models.FloatField(default=0.0)
    remaining = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee} - {self.start_date} to {self.end_date}: {self.total} days"

    class Meta:
        verbose_name = "Employee Sabbatical"
        verbose_name_plural = "Employee Sabbaticals"

class SabbaticalType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    max_days = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class SabbaticalRequest(models.Model):
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    sabbatical_type = models.ForeignKey(SabbaticalType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee} - {self.sabbatical_type} - {self.start_date} to {self.end_date}"
    
class SabbaticalApproval(models.Model):
    request = models.ForeignKey(SabbaticalRequest, on_delete=models.CASCADE)
    approver = models.ForeignKey('employees.Employee', on_delete=models.CASCADE, related_name='approvals')
    status = models.CharField(max_length=20, choices=[('approved', 'Approved'), ('rejected', 'Rejected')])
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.request} - {self.approver} - {self.status}"