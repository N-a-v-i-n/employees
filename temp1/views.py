from django.shortcuts import render
from .models import roles,department,employee,otp_verifing
from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
import random

# Create your views here.


def index(request):
    return render(request,"index.html")  # render(request, 'path/path')

def view_all(request):
    employees=employee.objects.all()
    context={
        "employee":employees
    }
    print(context)
    return render(request,'view_all.html',context)

def add_emp(request):
    if request.method=='POST':
        first_name1=request.POST['first_name1']
        last_name1=request.POST['last_name1']
        phone_no=request.POST['phone_no']
        email_id=request.POST['email_id']
        dept=request.POST['dept']
        role=request.POST['role']
        hire_date=request.POST['hire_date']

        new_emp=employee(
            first_name=first_name1,
            last_name=last_name1,
            phone_no=phone_no,
            email_id=email_id,
            dept=dept,
            role=role,
            hire_date=hire_date )
        new_emp.save()
        # otp_sent=otp_ver()
        # new_otp=otp_verifing(
        #     otp_sent=otp_sent,
        #     otp_sent_mail=email_id
        # )
        # new_otp.save()
        
        # send_mail("OTP Verify !!", f"Your otp is {otp_sent} " , settings.EMAIL_HOST_USER, [email_id], fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
        # context={"temp":[email_id]}
        # return render(request,'otp_verifing.html',context)

    return render(request,'add_emp.html')

def otp_ver():
    list_of_num = [0,1,2,3,4,5,6,7,8,9]
    otp_generate=set()
    while len(otp_generate)<5:
        otp_generate.add(random.choice(list_of_num))
    return ''.join(map(str,otp_generate))
  

def otp_verify(request):

    if request.method =='POST':
        otp_match=request.POST['otp_verify1']
        otp_email=request.POST['otp_email1']
        print("otp_match & otp_email : ",otp_match,otp_email)
        tempo=[]
        tempo.append(otp_verifing.objects.filter(otp_sent_mail=otp_email).values_list())
        print(tempo[0][0][2])
        if int(otp_match)==int(tempo[0][0][2]):

            return HttpResponse("OTP Verified And USER ADDED")
        else:
            remove_email=employee.objects.filter(email_id=otp_email).delete()
            remove_otp=otp_verifing.objects.filter(otp_sent_mail=otp_email).delete()
            return HttpResponse("OTP Not Match")
   
    return render(request,'otp_verifing.html')
        

def filter_emp(request):
    if request.method=='POST':
        search=request.POST["emp_name"]
        search2=request.POST["emp_mobile"]
        search1=request.POST["emp_id"]

        if request.POST["emp_name"] !="" and str(employee.objects.filter(first_name=search)) != "<QuerySet []>":
            searching = employee.objects.filter(first_name=search)
            context={"searched":searching}
            return render(request,"filter_emp.html",context)
        elif request.POST["emp_mobile"] !="" and str(employee.objects.filter(phone_no=search2)) != "<QuerySet []>":
            
            searching=employee.objects.filter(phone_no=search2)
            context={"searched":searching}
            return render(request,"filter_emp.html",context)
        elif request.POST["emp_id"] !="" and str(employee.objects.filter(id=search1)) != "<QuerySet []>":
            searching=employee.objects.filter(id=search1)
            context={"searched":searching}
            return render(request,"filter_emp.html",context)
        
        else:
             return HttpResponse(" Data Not Found ")

        # try:
        #     context={"searched":searching}
        #     return render(request,"filter_emp.html",context)
        # except:
        #     return HttpResponse("Data Not Found")

    elif request.method=='GET' :
        return render(request,'filter_emp.html')


def delete_emp(request):
  
    if request.method=='POST':
        data_received=request.POST['email_id']
        if str(employee.objects.filter(email_id=data_received)) != "<QuerySet []>" :
            print("EMP Found")
            del_emp=employee.objects.filter(email_id=data_received)
            # print(del_emp)
            del_emp.delete()
            # print(employee.objects.filter(email_id=data_received))
            return HttpResponse("Employee Successfully Removed")
        else:
            return HttpResponse("Employee Details Not Found")


    return render(request,'delete_emp.html')
    
def update_emp(request,employee_id):
    if  request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email_id=request.POST['email_id']
        updated_emp=employee.objects.filter(id=employee_id).update( 
            first_name=first_name,
            last_name=last_name,
            email_id=email_id
        )
        return HttpResponse("Successfully Updated")
    # elif request.method=="GET":
    #     return render(request,"update_emp.html")


    searching = employee.objects.filter(id=employee_id)
    context={"searched":searching}
    return render(request,"update_emp.html",context)



# def id(request):
#     return render(request,'update_emp.html')
