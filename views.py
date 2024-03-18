from django.shortcuts import render , HttpResponse
from .models import Employee
from datetime import datetime

# Create your views here.
def home (request):
    return render(request , "home.html")



def viewE (request):
    Alldetails = Employee.objects.all()
    context = {'Alldetails':Alldetails}
    return render(request , "viewE.html" , context)


def AddE(request):
    return render(request , "AddE.html")


def AddDetails(request):
    if request.method == 'POST':
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        Department = request.POST['Department']
        Salary = request.POST['Salary']
        Bonus = request.POST['Bonus']
        Role = request.POST['Role']
        phone = request.POST['phone']
        TosaveDetails = Employee(first_name = first_name , last_name = last_name , dept_id = Department , salary = Salary , bonus = Bonus , role_id = Role , phone = phone , hire_date = datetime.now())
        TosaveDetails.save()
        return render(request , "home.html")
    else:
        return HttpResponse("Failed to Add The Details of Employee")
    
    
    
def RemoveE(request):
    Alldetails = Employee.objects.all()
    context = {'Alldetails':Alldetails}
    return render(request , "RemoveE.html" , context)


def RemoveEmployee(request , id):
    Employee_id = Employee.objects.get(sno = id)
    Employee_id.delete()
    return render(request , "home.html")



def FilterE(request):
    return render(request ,'FilterE.html')

def FilterE1(request):
        query = request.GET['query']
        allEmployees_title = Employee.objects.filter(first_name__icontains = query)
        allEmployees_content = Employee.objects.filter(last_name__icontains = query)
        allEmployees_content = Employee.objects.filter(phone__icontains = query)
        Alldetails = allEmployees_title.union(allEmployees_content)
        
        context = {'Alldetails':Alldetails , 'query':query}
        return render(request , "viewE.html" , context)  