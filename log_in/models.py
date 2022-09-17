from django.db import models

class Subjects(models.Model):
    Id = models.CharField(max_length=40, primary_key=True)
    Name = models.CharField(max_length=64)
    Credit = models.CharField(max_length=1)
    Term = models.CharField(max_length=1, default='1')
    Year = models.CharField(max_length=4, default='2022')
    remainSeat = models.IntegerField(max_length=2, default=0)

    def __str__(self):
        return f"{self.subId}: {self.subName} term {self.subTerm} year {self.subYear} (remain seat = {self.remainseat})"

class Student(models.Model):
    courses = models.ManyToManyField(Subjects)
