from imp import IMP_HOOK
from multiprocessing import context
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

from log_in.models import Course
from log_in.models import Subject

def index(request):
   Subjects = Subject.objects.all() 
   template = loader.get_template('pages/index.html')
   context = {'Subjects': Subjects,}
   return HttpResponse(template.render(context, request))

def quota(request):
   Courses = Course.objects.all() 
   template = loader.get_template('pages/quota.html')
   context = {'Courses': Courses,}
   return HttpResponse(template.render(context, request))

def summit(request):
   if request.method == "POST":
      sub = Subject.objects.get(pk=Id)
      if sub not in Course.course.all():
         if sub.remainSeat != 0:
            Subject.objects.filter().update(remainSeat= sub.remainSeat - 1)
      Course.course.add(sub)