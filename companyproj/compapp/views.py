from django.shortcuts import render, redirect
from .models import Employee, Project
from django.utils import timezone
from .forms import EmployeeForm, ProjectForm 
from django.utils.text import slugify
# Create your views here.

def employee_list(request):
    employees = Employee.objects.all().order_by('name')
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    today = timezone.now().date()
    projects = employee.projects.filter(start_date__lte=today, 
                                        end_date__gte=today  )
    
    #projects = employee.projects.all()
    return render(request, 'employee_detail.html', 
                  {'employee': employee, 'projects': projects})

def employee_engineers(request):
    employees = Employee.objects.filter(position__icontains="engineer")
    return render(request, 'employee_list.html', {'employees': employees})

def add_employee(request):
    form=EmployeeForm(request.POST or None)
    data = {}
    data["form"] = form #4

    if form.is_valid(): #5
        employee=form.save(commit=False) #2
        
        
        return redirect("employee_list",) #7
    

    return render(request, 'add_employee.html', data)

def add_project(request):
    form=ProjectForm(request.POST or None)
    data = {}
    data["form"] = form #4

    if form.is_valid(): #5
        project=form.save(commit=False) #2
        project.save() #3
        
        return redirect("employee_list",) #7
    

    return render(request, 'add_project.html', data)