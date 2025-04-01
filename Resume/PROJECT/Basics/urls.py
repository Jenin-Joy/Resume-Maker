from Basics import views
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Calculator/',views.calculation,name="calculation"),
    path('Larsmall/',views.Larsmall,name="Largest"),
]
