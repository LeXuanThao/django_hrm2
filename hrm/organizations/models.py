from django.db import models
from django.utils.translation import gettext as _

class Department(models.Model):
    name = models.CharField(_("Department Name"), max_length=256, unique=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='sub_departments')
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    def __str__(self):
        return self.name
    
class Position(models.Model):
    name = models.CharField(_("Position Name"), max_length=256, unique=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='positions', null=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    def __str__(self):
        return self.name
    
class JobTitle(models.Model):
    name = models.CharField(_("Job Title"), max_length=256, unique=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='job_titles')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='job_titles')
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    def __str__(self):
        return self.name
    
class EmployeeInOrganization(models.Model):
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE, related_name='organizations')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name='employees')
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE, related_name='employees')
    start_date = models.DateField(_("Start Date"), blank=True)
    end_date = models.DateField(_("End Date"), blank=True, null=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    def __str__(self):
        return f"{self.employee} - {self.department} - {self.position} - {self.job_title}"