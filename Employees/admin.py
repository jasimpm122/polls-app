from django.contrib import admin
from Employees.models import Employee, Department, Manager, EmployeeLeave, EmployeeSalary

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Manager)
admin.site.register(EmployeeLeave)
admin.site.register(EmployeeSalary)