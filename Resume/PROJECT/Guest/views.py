from django.shortcuts import render
from django.shortcuts import render,redirect
from Guest.models import *
def UserRegistration(request):
    if request.method=="POST":
        if request.POST.get("txt_pass")==request.POST.get("txt_rpass"):   
            tbl_UserRegistration.objects.create( 
                UserRegistration_name=request.POST.get("txt_name"),  
                UserRegistration_email=request.POST.get("txt_email"),
                UserRegistration_password=request.POST.get("txt_pass"),
                UserRegistration_contact=request.POST.get("txt_phn"),
            )
            return render(request,"Guest/Login.html",{'msg':"registration sucessfull.."})

        else:
            return render(request,"Guest/Login.html",{'msg':"Password MisMatch.."})
    else:   
        return render (request,'Guest/Login.html')
def Login(request):
    if request.method=="POST":
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_pass")
        usercount=tbl_UserRegistration.objects.filter(UserRegistration_email=email,UserRegistration_password=password).count()
        if usercount>0:
            user=tbl_UserRegistration.objects.get(UserRegistration_email=email,UserRegistration_password=password)
            request.session['uid']=user.id
            return redirect("User:Homepage")
        else:
            return render(request,"Guest/Login.html",{'msg':"Invalid Email or Password"})
    else: 
        return render(request,"Guest/Login.html")
def index(request):
    return render(request,"Guest/index.html")