from django.shortcuts import render
from django.http import HttpResponse
def projecthomepage(request):
    return render(request, 'projecthomepage.html')

def employerhomepage(request):
    return render(request, 'employerhomepage.html')

def jobseekerhomepage(request):
    return render(request, 'jobseekerhomepage.html')

def signup(request):
    return render(request, 'signup.html')
from django.contrib import messages
from django.contrib.auth.models import User,auth
def signup1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully')
                return render(request, 'projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match')
            return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')
from django.shortcuts import render, redirect
def login1(request):
    if request.method== 'POST':
        username = request.POST['username']
        pass1=request.POST['password']
        user= auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            if len(username)==10:
                return redirect('jobseekerhomepage')
            elif len(username)==4:
                return redirect('employerhomepage')
            else:
                return redirect('projecthomepage')
        else:
            messages.info(request,'Invalid Credentials')
    else:
        return render(request,'login.html')




def logout(request):
    auth.logout(request)
    return render(request,'projecthomepage.html')

