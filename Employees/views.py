from django.shortcuts import render, HttpResponse, redirect, reverse
from Employees.models import Manager, Employee, Department, EmployeeSalary, EmployeeLeave
from Employees.forms import EmployeeForm


def managers_list(request):
    managers = Manager.objects.values()
    return HttpResponse(managers, safe=False)


def employees_list(request):
    employees = Employee.objects.all()
    return render(request, "llist.html", {
        'object': employees
    })


def leave_list(request):
    a = EmployeeLeave.objects.values()
    return HttpResponse(a, safe=False)


def salary_list(request):
    b = EmployeeSalary.objects.values()
    return HttpResponse(b, safe=False)


def delete_employee(request, employee_id):
    c = Employee.objects.get(id=employee_id)
    c.delete()
    return redirect(reverse('llist_employees'))


def add_employee(request):
    if request.method == 'GET':
        form = EmployeeForm()
        return render(request, 'add.html', {'form': form})
    elif request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list.html')


