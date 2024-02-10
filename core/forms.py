from django import forms
from .models import Course, Student, Teacher, Employee
from core.models import Employee 
from core.models import Teacher


# Курсы форма
class CourseForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())  # Замените на имя поля, которое вы хотите использовать


    class Meta:
        model = Course
        fields = ['name', 'price','date_start','date_end', 'teacher', 'employee']



# Студент форма
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email'] 

# Учитель форма
class TeacherForm(forms.ModelForm):
    courses_taught = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), required=False)

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name' ,'courses_taught']

