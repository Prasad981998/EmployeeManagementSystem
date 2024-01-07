from django.shortcuts import render
from .models import Employee,Role,Department
from .forms import AddEmployee   
from django.http import HttpResponse 

# Create your views here.
def index(request):
    return render(request,'employee/index.html')

def all_emp(request):
    emps=Employee.objects.all()
    return render(request,'employee/view_all_emp.html',{'employee':emps})

def add_emp(request):
    if request.method=='POST':
        fm=AddEmployee(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse("Employee Added Successfully") 
    else:
        fm=AddEmployee()
    return render(request,'employee/add_emp.html',{'form':fm})

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            employee_to_be_removed=Employee.objects.get(id=emp_id)
            employee_to_be_removed.delete()
            return HttpResponse("employee deleted successfully")
        except:
            return HttpResponse("please enter valid id")
    emps=Employee.objects.all()
    return render(request,'employee/remove_emp.html',{'emps':emps})


       
        
    
