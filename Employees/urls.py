from django.urls import path
from Employees.views import employees_list, add_employee, delete_employee

urlpatterns = [
    path("list/", employees_list, name='llist_employees'),
    path("add/", add_employee, name='aadd_employee'),
    path("delete/<int:employee_id>/", delete_employee, name='ddelete_employee')
]
