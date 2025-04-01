from django.contrib import admin
from django.urls import path
from Administrator import views
app_name="Administrator"
urlpatterns = [
    path('Admin Registration/',views.Administrator,name="Administrator"),
    path('District/', views.district, name="district"),
    path("Deletedistrict/<int:id>",views.deletedistrict,name="deletedistrict"),
    path("Homepage/",views.Homepage,name="Homepage"),
    path("editdistrict/<int:id>",views.editdistrict,name="editdistrict"),
    path('Language/', views.Language, name="language"),
    path("editlanguage/<int:id>",views.editlanguage,name="editlanguage"),
    path("deletelanguage/<int:id>",views.deletelanguage,name="deletelanguage"),
    path("Viewusers/",views.Viewusers,name="Viewusers"),
    path("Viewfeedback/",views.Viewfeedback,name="Viewfeedback"),
    path("Temp/",views.Temp,name="Temp"),
    path("Education/",views.Education,name="Education"),
    path("course/",views.course,name="course"),

]