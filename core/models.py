from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import qrcode
from io import BytesIO
from PIL import Image , ImageDraw
from django.core.files import File


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
    name = models.CharField(max_length=100, verbose_name='Ф.И.О')
    course = models.ManyToManyField(Course, related_name= 'students', verbose_name='Курс')
    status = models.IntegerField(choices=StudentStatus.choices, default=1, verbose_name='Статус')
    phone = models.CharField(max_length=255, verbose_name='Номер телефона')
    qr_code = models.ImageField(upload_to= 'students_qr/', blank=True)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname =f'qr_code-{self.name}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname,File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs) 


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


