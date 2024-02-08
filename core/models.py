from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Курс обучения')
    price = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Цена')

    class Meta:
        verbose_name = 'Курс'  
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    position = models.CharField(max_length=50, verbose_name='Должность')
    courses = models.ManyToManyField(Course, verbose_name='Курс обучения')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()


class Attendance(models.Model):
    date = models.DateField()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Teacher(Employee):
    speciality = models.CharField(max_length=100)


class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    category = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    class Meta:
        verbose_name = 'Группа'  
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name




