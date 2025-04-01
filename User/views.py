from django.shortcuts import render
from django.shortcuts import render,redirect
from User.models import *
from Guest.models import *
from Administrator.models import *
def ajaxcourse(request):
    course=tbl_course.objects.filter(educationtype=request.GET.get("did"))
    return render(request,"User/AjaxCourse.html",{'course':course})

def Homepage(request):
    if request.method=="POST":
        return redirect("User/Homepage.html")
    else:
        return render(request,"User/Homepage.html")
from django.shortcuts import render, redirect
from .models import tbl_certificate, tbl_UserRegistration

def Certificate(request):
    user_id = request.session.get('uid')  # Retrieve user ID from session
    data = tbl_certificate.objects.filter(user_id=user_id)
    if request.method == "POST":
        name = request.POST.get("txt_name")
        upload = request.FILES.get("file_photo")

    
        tbl_certificate.objects.create(
            certificate_name=name,
            certificate_upload=upload,
            user=tbl_UserRegistration.objects.get(id=request.session['uid'])
         ) 
        return redirect("User:Certificate")  # Redirect back to the certificate page

    return render(request, "User/Certificate.html", {"certificates": data})


def about(request):
    user_id = request.session.get('uid')  # Retrieve user ID from session
    data = tbl_about.objects.filter(user_id=user_id)  # Fetch only this user's data

    if request.method == "POST":
        about_text = request.POST.get("txt_about")
        tbl_about.objects.create(
            about_name=about_text,
            user=tbl_UserRegistration.objects.get(id=user_id)  # Associate entry with user
        ) 
        return redirect("User:Education")

    return render(request, "User/about.html", {"about": data})


def Education(request):
    educationtype = tbl_educationtype.objects.all()
    user = tbl_UserRegistration.objects.get(id=request.session['uid'])
    
    # Fetch all education records for the logged-in user
    education = tbl_Education.objects.filter(user=user)

    if request.method == "POST":
        tbl_Education.objects.create( 
            Education_Institution=request.POST.get("txt_institution"),
            Education_Course=tbl_course.objects.get(id=request.POST.get("sel_course")),
            Education_StartDate=request.POST.get("txt_Startdate"),
            Education_EndDate=request.POST.get("txt_Enddate"),
            user=user
        )
        return redirect("User:Education")

    return render(request, "User/Education.html", {
        'educationtype': educationtype,
        'education': education  # Add education records to context
    })


from django.shortcuts import render, redirect
from .models import tbl_Experience, tbl_UserRegistration

def Experience(request):
    if request.method == "POST":
        tbl_Experience.objects.create( 
            Experience_Jobtitle=request.POST.get("txt_Title"),
            Experience_Companyname=request.POST.get("txt_Companyname"),
            Experience_Experience=request.POST.get("txt_Experience"),
            Experience_Startdate=request.POST.get("txt_Startdate"),
            Experience_Enddate=request.POST.get("txt_Enddate"),
            Experience_Description=request.POST.get("txt_Description"),  
            user=tbl_UserRegistration.objects.get(id=request.session['uid'])
        )
        return redirect("User:Experience")

    # Fetch user's experience records
    experiences = tbl_Experience.objects.filter(user_id=request.session['uid'])

    return render(request, "User/Experience.html", {"experiences": experiences})

def Project(request):
    if request.method == "POST":
        tbl_Project.objects.create(
            Project_Name=request.POST.get("txt_Name"),
            Project_Details=request.POST.get("txt_Details"),
            Project_Link=request.POST.get("txt_link"),
            user=tbl_UserRegistration.objects.get(id=request.session['uid'])
        )
        return redirect("User:Project")

    # Fetch all projects for the logged-in user
    projects = tbl_Project.objects.filter(user__id=request.session['uid'])

    return render(request, "User/Project.html", {"projects": projects})     
def Language(request):
    user_id = request.session.get('uid')  # Retrieve user ID from session
    data = tbl_language.objects.filter(user_id=user_id)  # Fetch only this user's languages

    if request.method == "POST":
        language = request.POST.get("txt_Name")
        level = request.POST.get("Level")

        tbl_language.objects.create(
            language_name=language,
            language_level=level,
            user=tbl_UserRegistration.objects.get(id=user_id)  # Associate with the logged-in user
        ) 
        return redirect("User:Language")

    return render(request, "User/Language.html", {"languages": data})  # Pass data to the template

def Hobbies(request):
    user_id = request.session.get('uid')  # Retrieve user ID from session
    data = tbl_hobbies.objects.filter(user_id=user_id)  # Fetch hobbies for logged-in user

    if request.method == "POST":
        hobbies = request.POST.get("txt_Hobbies")  # Get hobby input
        tbl_hobbies.objects.create(
            hobbies_name=hobbies,
            user=tbl_UserRegistration.objects.get(id=user_id)  # Associate with user
        ) 
        return redirect("User:Hobbies")  # Redirect back to hobbies page

    return render(request, "User/Hobbies.html", {"hobbies": data})  # Pass hobbies data to template
 

def skill(request):
    user_id = request.session.get('uid')  # Retrieve user ID from session
    skills = tbl_skill.objects.filter(user_id=user_id)  # Fetch only this user's skills

    if request.method == "POST":
        skill_text = request.POST.get("txt_content")
        tbl_skill.objects.create(
            skill_name=skill_text,
            user=tbl_UserRegistration.objects.get(id=user_id)  # Associate skill with user
        )
        return redirect("User:skill")

    return render(request, "User/skill.html", {"skills": skills})  # Pass user skills to template



def Reference(request):
    user_id = request.session.get('uid')  # Retrieve user ID from session
    references = tbl_reference.objects.filter(user_id=user_id)  # Fetch only this user's references

    if request.method == "POST":
        Name = request.POST.get("txt_name")
        Email = request.POST.get("txt_email")
        Contact = request.POST.get("txt_contact")
        Relation = request.POST.get("txt_relation")

        tbl_reference.objects.create(
            reference_name=Name,
            reference_email=Email,
            reference_contact=Contact,
            reference_relation=Relation,
            user=tbl_UserRegistration.objects.get(id=user_id)  # Associate with user
        ) 
        return redirect("User:Reference")

    return render(request, "User/Reference.html", {"references": references})  
def Myprofile(request):
    user=tbl_UserRegistration.objects.get(id=request.session['uid'])
    return render(request,"User/Myprofile.html",{'user':user})
def Changepassword(request):
    user=tbl_UserRegistration.objects.get(id=request.session['uid'])
    userpassword=user.UserRegistration_password
    if request.method=="POST":
        oldpassword=request.POST.get("txt_opass")
        newpassword=request.POST.get("txt_npass")
        confirmpassword=request.POST.get("txt_cpass")
        if userpassword==oldpassword:
            if newpassword==confirmpassword:
                user.UserRegistration_password=newpassword
                user.save()
                return redirect("User:Myprofile")
            else:
                return render(request,"User/Changepassword.html",{'msg':"Password mismatch"})
        else:
            return render(request,"User/Changepassword.html",{'msg':"Password incorrect"})
    else:
        return render(request,"User/Changepassword.html")
def Editprofile(request):
    ed=tbl_UserRegistration.objects.get(id=request.session['uid'])
    if request.method=="POST":
        ed.UserRegistration_name=request.POST.get("txt_name")
        ed.UserRegistration_email=request.POST.get("txt_email")
        ed.UserRegistration_contact=request.POST.get("txt_contact")
        ed.save()
        return redirect("User:Myprofile")
    else:
        return render (request,'User/Editprofile.html',{'edit':ed})
    
def R1(request):
    user = tbl_UserRegistration.objects.get(id=request.session['uid'])
    
    certificates = tbl_certificate.objects.filter(user=user)
    education = tbl_Education.objects.filter(user=user)
    experience = tbl_Experience.objects.filter(user=user)
    projects = tbl_Project.objects.filter(user=user)
    languages = tbl_language.objects.filter(user=user)
    hobbies = tbl_hobbies.objects.filter(user=user)
    skills = tbl_skill.objects.filter(user=user)
    references = tbl_reference.objects.filter(user=user)
    about = tbl_about.objects.filter(user=user)

    context = {
        'user': user,
        'certificates': certificates,
        'education': education,
        'experience': experience,
        'projects': projects,
        'languages': languages,
        'hobbies': hobbies,
        'skills': skills,
        'references': references,
        'about': about,
    }

    return render(request, "User/R1.html", context)
def R2(request):
    user = tbl_UserRegistration.objects.get(id=request.session['uid'])
    
    certificates = tbl_certificate.objects.filter(user=user)
    education = tbl_Education.objects.filter(user=user)
    experience = tbl_Experience.objects.filter(user=user)
    projects = tbl_Project.objects.filter(user=user)
    languages = tbl_language.objects.filter(user=user)
    hobbies = tbl_hobbies.objects.filter(user=user)
    skills = tbl_skill.objects.filter(user=user)
    references = tbl_reference.objects.filter(user=user)
    about = tbl_about.objects.filter(user=user)
    context = {
        'user': user,
        'certificates': certificates,
        'education': education,
        'experience': experience,
        'projects': projects,
        'languages': languages,
        'hobbies': hobbies,
        'skills': skills,
        'references': references,
        'about': about,
    }

    return render(request, "User/R2.html", context)


def R3(request):
    user = tbl_UserRegistration.objects.get(id=request.session['uid'])
    
    certificates = tbl_certificate.objects.filter(user=user)
    education = tbl_Education.objects.filter(user=user)
    experience = tbl_Experience.objects.filter(user=user)
    projects = tbl_Project.objects.filter(user=user)
    languages = tbl_language.objects.filter(user=user)
    hobbies = tbl_hobbies.objects.filter(user=user)
    skills = tbl_skill.objects.filter(user=user)
    references = tbl_reference.objects.filter(user=user)
    about = tbl_about.objects.filter(user=user)
    context = {
        'user': user,
        'certificates': certificates,
        'education': education,
        'experience': experience,
        'projects': projects,
        'languages': languages,
        'hobbies': hobbies,
        'skills': skills,
        'references': references,
        'about': about,
    }

    return render(request, "User/R3.html", context)

def R4(request):
    user = tbl_UserRegistration.objects.get(id=request.session['uid'])
    
    certificates = tbl_certificate.objects.filter(user=user)
    education = tbl_Education.objects.filter(user=user)
    experience = tbl_Experience.objects.filter(user=user)
    projects = tbl_Project.objects.filter(user=user)
    languages = tbl_language.objects.filter(user=user)
    hobbies = tbl_hobbies.objects.filter(user=user)
    skills = tbl_skill.objects.filter(user=user)
    references = tbl_reference.objects.filter(user=user)
    about = tbl_about.objects.filter(user=user)
    context = {
        'user': user,
        'certificates': certificates,
        'education': education,
        'experience': experience,
        'projects': projects,
        'languages': languages,
        'hobbies': hobbies,
        'skills': skills,
        'references': references,
        'about': about,
    }

    return render(request, "User/R4.html", context)

def R5(request):
    user = tbl_UserRegistration.objects.get(id=request.session['uid'])
    
    certificates = tbl_certificate.objects.filter(user=user)
    education = tbl_Education.objects.filter(user=user)
    experience = tbl_Experience.objects.filter(user=user)
    projects = tbl_Project.objects.filter(user=user)
    languages = tbl_language.objects.filter(user=user)
    hobbies = tbl_hobbies.objects.filter(user=user)
    skills = tbl_skill.objects.filter(user=user)
    references = tbl_reference.objects.filter(user=user)
    about = tbl_about.objects.filter(user=user)
    context = {
        'user': user,
        'certificates': certificates,
        'education': education,
        'experience': experience,
        'projects': projects,
        'languages': languages,
        'hobbies': hobbies,
        'skills': skills,
        'references': references,
        'about': about,
    }

    return render(request, "User/R5.html", context)

def Choose(request):
    if request.method=="POST":
        return redirect("User/Choose.html")
    else:
        return render(request,"User/Choose.html")
    
def T1(request):
    certificate = tbl_certificate.objects.filter(user=request.session["uid"])
    reference = tbl_reference.objects.filter(user=request.session["uid"])
    hobbies = tbl_hobbies.objects.filter(user=request.session["uid"])
    about_name = tbl_about.objects.filter(user=request.session["uid"])
    language = tbl_language.objects.filter(user=request.session["uid"])
    skill = tbl_skill.objects.filter(user=request.session["uid"])
    project = tbl_Project.objects.filter(user=request.session["uid"])
    experience = tbl_Experience.objects.filter(user=request.session["uid"])
    education = tbl_Education.objects.filter(user=request.session["uid"])
    user = tbl_UserRegistration.objects.get(id=request.session["uid"])
    if request.method=="POST":
        return redirect("User/T1.html")
    else:
        return render(request,"User/T1.html",{"certificate":certificate,"reference":reference,"hobbies":hobbies,"language":language,"skill":skill,"project":project,"experience":experience,"education":education,"about":about_name,"user":user})
    
def cv(request):
    data=tbl_cv.objects.filter(user=request.session['uid'])
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        about=request.POST.get("txt_about")
        education=request.POST.get("txt_education")
        experience=request.POST.get("txt_experience")
        skill=request.POST.get("txt_skill")
        hobbies=request.POST.get("txt_hobbies")
        reference=request.POST.get("txt_references")
        language=request.POST.get("txt_language")
        project=request.POST.get("txt_project")
        certificate=request.POST.get("txt_certificate")
        tbl_cv.objects.create(
            cv_name=name,
            cv_email=email,
            cv_contact=contact,
            cv_address=address,
            cv_about=about,
            cv_education=education,
            cv_experience=experience,
            cv_skill=skill,
            cv_hobbies=hobbies,
            cv_reference=reference,
            cv_language=language,
            cv_project=project,
            cv_certificate=certificate,
            user=tbl_UserRegistration.objects.get(id=request.session['uid'])
        ) 
        return redirect("User:Choose1")
    else:
        return render(request,"User/cv.html",{'data':data})
def C1(request):
    cv = tbl_cv.objects.filter(user=request.session['uid']).first()  
    return render(request, "User/C1.html", {'cv': cv})
def C2(request):
    cv = tbl_cv.objects.filter(user=request.session['uid']).first() 
    return render(request, "User/C2.html", {'cv':cv})
def C3(request):
    cv = tbl_cv.objects.filter(user=request.session['uid']).first() 
    return render(request, "User/C3.html", {'cv':cv})
def C4(request):
    cv = tbl_cv.objects.filter(user=request.session['uid']).first() 
    return render(request, "User/C4.html", {'cv':cv})
def C5(request):
    cv = tbl_cv.objects.filter(user=request.session['uid']).first() 
    return render(request, "User/C5.html", {'cv':cv})
def Customization(request):
    if request.method=="POST":
        return redirect("User/Customization.html")
    else:
        return render(request,"User/Customization.html")

def Choose1(request):
    if request.method=="POST":
        return redirect("User/Choose1.html")
    else:
        return render(request,"User/Choose1.html")
def Feedback(request):
    if request.method=="POST":  
        tbl_Feedback.objects.create( 
            Feedback_name=request.POST.get("txt_name"),  
            Feedback_email=request.POST.get("txt_email"),
            Feedback_message=request.POST.get("txt_message"),
            user=tbl_UserRegistration.objects.get(id=request.session['uid'])
        )
        return render(request,'User/Feedback.html')
    else:   
        return render(request,'User/Feedback.html')
    
def edit_about(request, id):
    about_entry = tbl_about.objects.get(id=id)  # Get the specific "About Me" entry

    if request.method == "POST":
        updated_text = request.POST.get("txt_about")
        about_entry.about_name = updated_text  # Update the content
        about_entry.save()  # Save the changes
        return redirect("User:about")  # Redirect to the About Me page

    return render(request, "User/about.html", {"edit": about_entry})
def deleteabout(request,id):
    tbl_about.objects.get(id=id).delete()
    return redirect("User:about")

def deleteeducation(request,id):
    tbl_Education.objects.get(id=id).delete()
    return redirect("User:Education")


def delete_experience(request,id):
    tbl_Experience.objects.get(id=id).delete()
    return redirect("User:Experience")

def delete_skill(request,id):
    tbl_skill.objects.get(id=id).delete()
    return redirect("User:skill")

def delete_hobby(request,id):
    tbl_hobbies.objects.get(id=id).delete()
    return redirect("User:Hobbies")


def delete_reference(request,id):
    tbl_reference.objects.get(id=id).delete()
    return redirect("User:Reference")

def delete_language(request, id):
    tbl_language.objects.get(id=id).delete()
    return redirect("User:Language")

def delete_project(request, id):
    tbl_Project.objects.get(id=id).delete()
    return redirect("User:Project")

def delete_certificate(request, id):
    tbl_certificate.objects.get(id=id).delete()
    return redirect("User:Certificate")