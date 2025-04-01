from django.shortcuts import render

# Create your views here.
def calculation(request):
    if request.method=="POST":
        a=int(request.POST.get('txt_no1'))
        b=int(request.POST.get('txt_no2'))
        btn=request.POST.get('btnsubmit')
        if btn=="+":
            result=a+b
        elif btn=="-":
            result=a-b
        elif btn=="*":
            result=a*b
        else:
            result=a/b
        return render(request,"Basics/Calculator.html",{'res':result})
    else:
        return render(request,"Basics/Calculator.html")

def Larsmall(request):
    if request.method=="POST":
        a=int(request.POST.get('txt_no1'))
        b=int(request.POST.get('txt_no2'))
        btn=request.POST.get('btnsubmit')
        if a>b:
            Largest=a
            Smallest=b
           
        else:
            Largest=b
            Smallest=a
        return render(request,"Basics/Larsmall.html",{'l':Largest,'s':Smallest})
        
    else:
        return render(request,"Basics/Larsmall.html")
       