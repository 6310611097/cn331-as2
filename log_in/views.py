from logging import Filter
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login 
from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse

from log_in.models import Course
from log_in.models import Subject

def index(request):         
    Subjects = Subject.objects.all() 
    template = loader.get_template('pages/index.html')
    context = {'Subjects': Subjects,}
    if request.method != "POST":
        return HttpResponse(template.render(context, request))
    if request.method == "POST":
        sub_id = request.POST["sub"]
        sub = Subject.objects.get(Id=sub_id)
        if not Course.objects.filter(Id=sub_id).exists():
            Course.objects.create(Id=sub.Id, Name=sub.Name, Credit=sub.Credit)
            Subject.objects.filter(Id=sub_id).update(remainSeat=sub.remainSeat - 1)
            messages.success(request, ("Congratuation, You have enrolled "+sub_id))
        else:
            messages.success(request, ("You already enrolled "+sub_id))
        return redirect('/home')
    elif request.method == "GET":
        return render(request, 'pages/index.html')

def quota(request):
    Courses = Course.objects.all() 
    template = loader.get_template('pages/quota.html')
    context = {'Courses': Courses,}
    if request.method != "POST":
        return HttpResponse(template.render(context, request))
    if request.method == "POST":
        cou_id = request.POST["cou"]
        sub = Subject.objects.get(Id=cou_id)
        Course.objects.filter(Id=cou_id).delete()
        Subject.objects.filter(Id=cou_id).update(remainSeat=sub.remainSeat + 1)
        messages.success(request, ("You have deleted "+cou_id))
        return redirect('/result')
    elif request.method == "GET":
        return render(request, 'pages/quota.html')
        

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/home')
        else:
            messages.success(request, ("Login fail, Please try again."))
            return redirect('/')
    else:
        return render(request, 'pages/login.html')
            