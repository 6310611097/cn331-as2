from re import template
from django.urls import reverse
from django.shortcuts import redirect
from django.test import TestCase, Client
from .models import Subject, Student

class testCode(TestCase):
    def setUp_Subject(self):
        sub = Subject.objects.create(
        ID = "CNXXX", 
        Name = "XXXXXX", 
        Credit = "3",
        Year = "2066",
        )
        Subject.save()
        self.assertEqual(str(sub), "CNXXX XXXXXX")

    def setUp_Student(self):
        user = Student.objects.create(
            first_name = "a",
            last_name = "pencil"
        )
        user.save()
        self.assertEqual(str(user), "a pencil")

    def test_reaminSeat_available(self):
        sub=Subject.objects.first()
        self.assertTrue(sub.is_seat_available())

    def test_login_page(self):
        cl = Client()
        web =cl.get(redirect('/'))
        self.assertEqual(web.status_code, 200)
    
    def test_index_page(self):
        cl = Client()
        web =cl.get(redirect('/home'))
        self.assertEqual(web.status_code, 200)

    def test_quota_page(self):
        cl = Client()
        web =cl.get(redirect('/result'))
        self.assertEqual(web.status_code, 200)

    def test_login(self):
        self.client = Client()
        web = self.client.get(redirect('/home'),{"username": "a", "password": "aaa11111"})
        web = self.client.get(redirect('/home'))
        self.assertEqual(web.status_code, 200)
        
