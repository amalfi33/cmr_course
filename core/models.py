from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Курс обучения')
    price = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Цена')
    date_start = models.DateField(verbose_name='Дата начала подписки')
    date_end = models.DateField(verbose_name='Дата конца подписки')

    class Meta:
        verbose_name = 'Курс'  
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    speciality = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учитель'

    def __str__(self):
        return self.speciality  

class Employee(models.Model):
    user = models.ManyToManyField(User)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    speciality = models.ManyToManyField(Teacher,verbose_name='Должность')
    courses = models.ManyToManyField(Course, verbose_name='Курс обучения')
    salary = models.IntegerField(verbose_name='Зарплата')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
    # Получаем первого пользователя, связанного с этим сотрудником
        user = self.user.first()
    # Если пользователь существует, возвращаем его имя, иначе пустую строку
        return f"{user if user else ''}"

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()


class Attendance(models.Model):
    date = models.DateField()


class Student(models.Model):
    class StudentStatus(models.IntegerChoices):
        active = 1 
        archived = 2

    name = models.CharField(max_length=100)
    course = models.ManyToManyField(Course, related_name= 'students')
    status = models.IntegerField(choices=StudentStatus.choices, default=1)
    phone = models.CharField(max_length=255)
    code = models.CharField(max_length=8, null = True)
    qr = models.ImageField(upload_to= 'students_qr/', null=True)


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

    

