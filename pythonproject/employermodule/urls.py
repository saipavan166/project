from django.contrib import admin
from django.urls import path
from . import views

app_name = 'employermodule'

urlpatterns = [
    path('jobpost/', views.jobpost, name='jobpost'),
    path('add_job_details/', views.add_job_details, name='add_job_details'),  # Added missing '/' in the URL
    path('views/', views.view_job_details, name='view_job_details'),
    path('edit/<int:job_id>/', views.editjobdetails, name='editjobdetails'),
    path('delete/<int:job_id>/', views.deletejobdetails, name='deletejobdetails'),
path('job_application_list/', views.job_application_list, name='job_application_list'),

]
