from django.db import models

class SpecialDate(models.Model):
    date = models.DateField(unique=True)
    is_holiday = models.BooleanField(default=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.date} - {self.description}"
    
class WorkType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class WorkSchedule(models.Model):
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=[(i, day) for i, day in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])])
    start_time = models.TimeField()
    end_time = models.TimeField()
    break_start_time = models.TimeField()
    break_end_time = models.TimeField()

    def __str__(self):
        return f"{self.work_type.name} - {self.day_of_week} - {self.start_time} to {self.end_time}"
    
class EmployeeWorkTime(models.Model):
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee.fullname} - {self.work_type.name}"
    
class AttendanceLog(models.Model):
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField(null=True, blank=True)
    work_schedule = models.ForeignKey(WorkSchedule, on_delete=models.CASCADE, null=True, blank=True)
    special_date = models.ForeignKey(SpecialDate, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.employee.fullname} - {self.check_in_time} to {self.check_out_time}"