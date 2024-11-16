from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q



def index(request):
    return render(request, 'website/index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'website/view_all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name= request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        role = int(request.POST['role']) 
        dept = int(request.POST['dept'])
        
        new_emp = Employee(first_name= first_name ,last_name= last_name,salary= salary, bonus=bonus, phone=phone, role_id = role ,dept_id =dept, hire_date = datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method== 'GET':
      return render(request, 'website/add_emp.html')
    else:
        return HttpResponse('An Exception Occured Employee Has not been added')


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse('Please Enter A valid Emp Id')
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'website/remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name'].strip()
        dept = request.POST['dept'].strip()
        role = request.POST['role'].strip()
        emps = Employee.objects.all()
       
        if name:
            emps_new = emps.filter(Q(first_name__icontains= name) | Q(last_name__icontains = name))
            
        if dept:
           emps_new = emps.filter(dept__name=dept)

        if role :
            emps_new = emps.filter(role__name = role)
        
        context = {
            'emps': emps_new
        
        }
        return render(request, 'website/view_all_emp.html', context)
    elif request.method == 'GET':
        return render(request, 'website/filter_emp.html')
    else:
        return HttpResponse('As Exception occured')


