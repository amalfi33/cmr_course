from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    # Дополнительные поля и методы

class Attendance(models.Model):
    date = models.DateField()
    # Дополнительные поля и методы

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Дополнительные поля и методы

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Дополнительные поля и методы

class Teacher(Employee):
    speciality = models.CharField(max_length=100)
    # Дополнительные поля и методы

class Category(models.Model):
    name = models.CharField(max_length=100)
    # Дополнительные поля и методы

class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    # Дополнительные поля и методы



