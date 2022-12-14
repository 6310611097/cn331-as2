from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    Id = models.CharField(max_length=10, primary_key=True)
    Name = models.CharField(max_length=64)
    Credit = models.CharField(max_length=1)
    Term = models.CharField(max_length=1, default='1')
    Year = models.CharField(max_length=4, default='2022')
    remainSeat = models.IntegerField(default=10)

    def __str__(self):
        return f"{ self.Id } { self.Name}"
    
    def is_seat_available(self):
        return self.remainSeat < 0

class Student(models.Model):
    courses = models.ManyToManyField(Subject)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def  __str__(self):
        return f"{ self.users.first_name } { self.users.last_name}"

class Course(models.Model):
    Id = models.CharField(max_length=10, primary_key=True)
    Name = models.CharField(max_length=64)
    Credit = models.CharField(max_length=1)
    Term = models.CharField(max_length=1, default='1')
    Year = models.CharField(max_length=4, default='2022')
