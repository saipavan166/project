from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Applicant, JobDetails
from .forms import JobApplicationForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

def viewjobs(request):
    job_details_list = JobDetails.objects.all()
    return render(request, 'jobseekermodule/viewjobs.html', {'job_details_list': job_details_list})

@login_required(login_url='login1')
def job_details_list(request):
    job_details_list = JobDetails.objects.all()
    return render(request, 'jobseekermodule/viewjobs.html', {'job_details_list': job_details_list})

def addjobseekerprofile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        phone_number = request.POST.get('phone_number', '')
        address = request.POST.get('address', '')
        tenth_marks = request.POST.get('tenth_marks', '')
        twelfth_marks = request.POST.get('twelfth_marks', '')
        cgpa = request.POST.get('cgpa', '')
        expected_salary = request.POST.get('expected_salary', '')
        position = request.POST.get('position', '')

        applicant = Applicant.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            tenth_marks=tenth_marks,
            twelfth_marks=twelfth_marks,
            cgpa=cgpa,
            expected_salary=expected_salary,
            position=position
        )

        return HttpResponseRedirect(reverse('jobseekermodule/view_jobs_details.html'))
    else:
        return render(request, 'jobseekermodule/addjobseekerprofile.html')

def submit_form(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job_application = form.save()
            job_application.save()

            subject = 'Job Application Received'
            message = 'Thank You for applying to the job. Your application is received and will be sent to the next process.'
            from_email = 'saipavan8641@gmail.com'
            recipient_list = [job_application.email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect('jobseekermodule:job_details_list')
    else:
        form = JobApplicationForm()
    return render(request, 'jobseekermodule/apply_to_job.html', {'form': form})

def apply_to_job(request, job_id):
    job_details = get_object_or_404(JobDetails, id=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.job_details = job_details
            job_application.save()

            subject = 'Job Application Received'
            message = 'Thank You for applying to the job. Your application is received and will be sent to the next process.'
            from_email = 'saipavan8641@gmail.com'
            recipient_list = [job_application.email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect('jobseekermodule:job_details_list')
    else:
        form = JobApplicationForm()
    return render(request, 'jobseekermodule/apply_to_job.html', {'job_details': job_details, 'form': form})
