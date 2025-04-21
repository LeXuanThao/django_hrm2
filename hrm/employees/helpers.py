from datetime import date

def get_seniority(employee):
    """
    Calculate the seniority of an employee in years.
    If the employee has a termination date, calculate the seniority until that date.
    Otherwise, calculate the seniority until today.
    """
    if employee.termination_date:
        return (employee.termination_date - employee.hire_date).days // 365
    return (date.today() - employee.hire_date).days // 365