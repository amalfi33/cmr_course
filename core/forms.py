from django import forms
from .models import Course, Teacher, Employee
from core.models import Employee 
from core.models import Teacher


# Курсы форма
class CourseForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())  # Замените на имя поля, которое вы хотите использовать


    class Meta:
        model = Course
        fields = ['name', 'price','date_start','date_end', 'teacher', 'employee']


# Учитель форма
class TeacherForm(forms.ModelForm):
    courses_taught = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), required=False)

    class Meta:
        model = Teacher
        fields = ['courses_taught']

