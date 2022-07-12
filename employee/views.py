from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .models import Employee
from django.db.models import Q

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render (request,"index.html")    

def filter_emp(request):
    if request.method=="POST":
        name = request.POST.get("name")
        role = request.POST.get("role")
        dept = request.POST.get("dept")
        emp =Employee.objects.all()

        if name:
            emps=emp.filter(Q(first_name__icontains=name)| Q(last_name__icontains=name))
        if role:
            emps=emp.filter(role__name__icontains=role)
        if dept:
            emps = emp.filter(dept__name__icontains=dept)

        context={
            'emps':emps
        }
        return render (request,'all_emp.html',context)
    return render (request,'filter_emp.html')

def add_emp(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        department=int(request.POST["department"])
        role=int(request.POST["role"])
        salary=int(request.POST["salary"])
        bonus=int(request.POST["bonus"])
        phone=int(request.POST["phone"])
        
        new_emp = Employee(first_name=first_name,last_name=last_name,dept_id=department,role_id=role,salary=salary,bonus=bonus,phone=phone,hire_date=datetime.now())
        print(new_emp)
        new_emp.save()
        return HttpResponse("New Employee has successfully added")

    return render (request,'add_emp.html')

def remove_emp(request,emp_id=0):
        if emp_id:
          try:
            emp_removed=Employee.objects.get(id=emp_id)
            emp_removed.delete()
            return HttpResponse("Employee Removed successfully")
          except:
            return HttpResponse("Please Enter A Valid Employee Id")

        emps= Employee.objects.all()
        context={
        'emps': emps
           }
        return render (request,'remove_emp.html',context)

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render (request,'all_emp.html',context)

def loginpage(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
    return render (request,"login.html")

def logoutpage(request):
    logout(request)
    return redirect("/login")