from django.shortcuts import render
from urllib import request

from log_in.models import Student
from log_in.models import Subjects

def index(request):
   return render(request, 'pages/index.html')

def quota(request):
   return render(request, 'pages/quota.html')

def quota(request):
   if request.method == "POST":
      sub = Subjects.objects.get(pk=Id)
      if sub not in Student.courses.all():
         if sub.remainSeat != 0:
            Subjects.objects.filter().update(remainSeat= sub.remainSeat - 1)
      Student.course.add(sub)