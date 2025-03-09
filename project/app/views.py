from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render,HttpResponse
# Create your views here.

@login_required
def some_view(request):
    if not request.user.groups.filter(name='Web Users').exists():
        return HttpResponse("You don't have permission to access this page.")
    return render(request, 'home.html')
def logout_view(request):
    logout(request)  # Clears the session and logs the user out
    return redirect('/') 
def show(request):
    return render(request,"home.html")

def all_stu(request):
    stud = Student.objects.all()
    context = {
        'studs': stud

    }
    print(context)
    return render(request,'viewstudent.html',context)
def index(request):
    data=Student.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)


def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/")

    return render(request,"index.html")


def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']

        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/")

    d=Student.objects.get(id=id) 
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=Student.objects.get(id=id) 
    d.delete()
    messages.error(request,"Data deleted Successfully")
    return redirect("/")
    
    




def angilalB(request):
    return render(request,"angilalB.html")

def angilalC(request):
    return render(request, "angilalC.html")

def angilalD(request):
    return render(request,"angilalD.html")

def angilalE(request):
    return render(request,"angilalE.html")

def uhat(request):
    return render(request,"uhat.html")

def uhzt(request):
    return render(request,"uhzt.html")

def aa(request):
    return render(request,"aa.html")

def jt(request):
    return render(request,"jt.html")

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')