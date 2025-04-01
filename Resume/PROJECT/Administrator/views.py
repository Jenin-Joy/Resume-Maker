from django.shortcuts import render,redirect
from Administrator.models import*
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
    return render(request,"Administrator/Homepage.html")
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
