from django import forms
from .models import Course, Student, Teacher, Employee , Position
from core.models import Employee
from django.contrib.auth.models import User
from core.models import Teacher


# Курсы форма
class CourseForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())  # Замените на имя поля, которое вы хотите использовать


    class Meta:
        model = Course
        fields = ['name', 'price','date_start','date_end', 'teacher', 'employee']


# Форма студента
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'course', 'status', 'phone'] 


# Учитель форма
class TeacherForm(forms.ModelForm):
    courses_taught = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), required=False)

    class Meta:
        model = Teacher
        fields = ['name']

# Форма авторизации
class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Логин', required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': "Логин"}))
    password = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': "Пароль"}))
    first_name = forms.CharField(label='Имя', required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': "Имя"}))
    last_name = forms.CharField(label='Фамилия', required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': "Фамилия"}))
    position = forms.ModelMultipleChoiceField(label='Должность', queryset=Position.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'form-control mb-3'}))
    phone = forms.CharField(label='Номер телефона', required=False, widget=forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': "Номер телефона"}))

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            employee = Employee.objects.create(
                user=user,
                phone=self.cleaned_data['phone'],
            )
        return user


