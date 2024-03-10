from django.shortcuts import render,get_object_or_404,redirect
from .models import JobDetails

def jobpost(request):
    return render(request, 'employermodule/jobpost.html')

def add_job_details(request):
    if request.method == 'POST':
        work_title = request.POST.get('workTitle')
        salary_offered = request.POST.get('salaryOffered')
        job_type = request.POST.get('jobType')
        benefits = request.POST.get('benefits')
        education = request.POST.get('education')
        work_location = request.POST.get('workLocation')
        required_skills = request.POST.get('requiredSkills')
        review = request.POST.get('review')

        job_details = JobDetails(
            work_title=work_title,
            salary_offered=salary_offered,
            job_type=job_type,
            benefits=benefits,
            education=education,
            work_location=work_location,
            required_skills=required_skills,
            review=review,
        )
        job_details.save()
        return render(request, 'employermodule/datainserted.html')
    return render(request, 'employermodule/jobpost.html')

def view_job_details(request):
    job_details_list=JobDetails.objects.all()
    return render(request,'employermodule/view_job_details.html',{'job_details_list':job_details_list})
def editjobdetails(request,job_id):
    job_details= get_object_or_404(JobDetails,id=job_id)
    if request.method=='POST':
        job_details.work_title = request.POST.get('workTitle')
        job_details.salary_offered = request.POST.get('salaryOffered')
        job_details.job_type = request.POST.get('jobType')
        job_details.benefits = request.POST.get('benefits')
        job_details.education = request.POST.get('education')
        job_details.work_location = request.POST.get('workLocation')
        job_details.required_skills = request.POST.get('requiredSkills')
        job_details.review = request.POST.get('review')
        job_details.save()
        return redirect('employermodule:view_job_details')
    return render(request,'employermodule/editjobdetails.html',{'job_details':job_details})


def deletejobdetails(request,job_id):
    job_details = get_object_or_404(JobDetails,id=job_id)
    if request.method=='POST':
        job_details.delete()
        return redirect('employermodule:view_job_details')
    return render(request, 'employermodule/deletejobdetails.html', {'job_details': job_details})



from jobseekermodule.models import *
def  job_application_list(request):
    job_applications=JobApplication.objects.all()
    return render(request,'employermodule/job_application_list.html',{'job_applications':job_applications})
