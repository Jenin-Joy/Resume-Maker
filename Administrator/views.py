from django.shortcuts import render,redirect
from Administrator.models import*
from User.models import *
from Guest.models import *
# Create your views here.
def Administrator(request):
    data=tbl_district.objects.all()
    if request.method=="POST":
        tbl_Administrator.objects.create(
            Administrator_name=request.POST.get("txt_name"),
            Administrator_email=request.POST.get("txt_email"),
            Administrator_password=request.POST.get("txt_password")
        )
        return render(request,'Administrator/Administration.html')
    else:
        return render(request,'Administrator/Administration.html')
def district(request):
    data=tbl_district.objects.all()
    if request.method=="POST":
        district=request.POST.get('txt_name')
        tbl_district.objects.create(
            district_name=district,
        )
        return render(request,"Administrator/District.html",{'data':data})
    else:
        return render(request,"Administrator/District.html",{'data':data})
def deletedistrict(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect("Administrator:district")
def editdistrict(request,id):
    ed=tbl_district.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("txt_name")
        ed.district_name=name
        ed.save()
        return redirect("Administrator:district")
    else:
        return render(request,"Administrator/District.html",{'edit':ed})
def Homepage(request):
    user=tbl_UserRegistration.objects.all()
    return render(request,"Administrator/Homepage.html",{'user':user})
def Language(request):
    data=tbl_language.objects.all()
    if request.method=="POST":
        language_name=request.POST.get('txt_name')
        tbl_language.objects.create(
            language=language_name,
        )
        return render(request,"Administrator/Language.html",{'data':data})
    else:
        return render(request,"Administrator/Language.html",{'data':data})
def deletelanguage(request,id):
    tbl_language.objects.get(id=id).delete()
    return redirect("Administrator:language")
def editlanguage(request,id):
    ed=tbl_language.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("txt_name")
        ed.language=name
        ed.save()
        return redirect("Administrator:language")
    else:
        return render(request,"Administrator/Language.html",{'edit':ed})
    
def Viewusers(request):
    user=tbl_UserRegistration.objects.all()
    return render(request,"Administrator/Viewusers.html",{'user':user})
def Viewfeedback(request):
    user=tbl_Feedback.objects.all()
    return render(request,"Administrator/Viewfeedback.html",{'user':user})
def Temp(request):
    # user=tbl_UserRegistration.objects.all()
    return render(request,"Administrator/Temp.html")
def Education(request):
    data=tbl_educationtype.objects.all()
    if request.method=="POST":
        tbl_educationtype.objects.create( 
            educationtype=request.POST.get("txt_Graduation"),  
            )
        return render (request,'Administrator/Education.html',{'data':data})
    else:   
        return render (request,'Administrator/Education.html',{'data':data})
def course(request):
    educationtype=tbl_educationtype.objects.all()
    if request.method == "POST":
        tbl_course.objects.create(
        course=request.POST.get("txt_course"),
        educationtype=tbl_educationtype.objects.get(id=request.POST.get("sel_education"))
        )
        return redirect("Administrator:course")
    else:
        return render(request,"Administrator/Course.html",{'educationtype':educationtype})
