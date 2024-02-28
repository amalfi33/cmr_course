from django import forms
from .models import Course, Student, Teacher, Employee , Position
from core.models import Employee
from django.contrib.auth.models import User
from core.models import Teacher


# Курсы форма
class CourseForm(forms.ModelForm):
    name = forms.CharField(label='Название Курса', required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'style': 'border: none; border-bottom: 2px solid #D1D1D4; 	background: none; padding: 10px; padding-left: 24px; font-weight: 700; width: 75%; transition: .2s; outline: none; border-bottom-color: #6A679E;    ', 'placeholder': "Название"})) 
    description = forms.CharField(label='Описание Курса', required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'style': 'border: none; border-bottom: 2px solid #D1D1D4; 	background: none; padding: 10px; padding-left: 24px; font-weight: 700; width: 75%; transition: .2s; outline: none; border-bottom-color: #6A679E;    ', 'placeholder': "Описание"}))
    price = forms.IntegerField(label='Цена Курса', required=True, widget=forms.NumberInput(attrs={'class': 'form-control mb-3', 'style': 'border: none; border-bottom: 2px solid #D1D1D4; 	background: none; padding: 10px; padding-left: 24px; font-weight: 700; width: 75%; transition: .2s; outline: none; border-bottom-color: #6A679E;    ', 'placeholder': "Цена"}))
    date_start = forms.DateField(label='Дата начала подписки', required=True, widget=forms.DateInput(attrs={'class': 'form-control mb-3', 'style': 'border: none; border-bottom: 2px solid #D1D1D4; 	background: none; padding: 10px; padding-left: 24px; font-weight: 700; width: 75%; transition: .2s; outline: none; border-bottom-color: #6A679E;    ', 'placeholder': "Дата начала подписки"})) 
    date_end = forms.DateField(label='Дата конца подписки', required=True, widget=forms.DateInput(attrs={'class': 'form-control mb-3', 'style': 'border: none; border-bottom: 2px solid #D1D1D4; 	background: none; padding: 10px; padding-left: 24px; font-weight: 700; width: 75%; transition: .2s; outline: none; border-bottom-color: #6A679E;    ', 'placeholder': "Дата конца подписки"}))       
    class Meta:
        model = Course
        fields = ['name', 'description', 'price' , 'date_start', 'date_end']


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
        fields = ['user']

# Форма авторизации
class EmployeeCreationForm(forms.ModelForm):
    username = forms.CharField(label='Логин', required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'style': 'border: none; border-bottom: 2px solid #D1D1D4; 	background: none; padding: 10px; padding-left: 24px; font-weight: 700; width: 75%; transition: .2s; outline: none; border-bottom-color: #6A679E;    ', 'placeholder': "Логин"})) 
    password = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'style': 'border: none; border-bottom: 2px solid #D1D1D4; background: none; padding: 10px; padding-left: 24px; font-weight: 700; width: 75%;  transition: .2s; outline: none; border-bottom-color: #6A679E;', 'placeholder': "Пароль"}))
    first_name = forms.CharField(label='Имя', required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'style': 'border: none; border-bottom: 2px solid #D1D1D4; 	background: none; padding: 10px; padding-left: 24px; font-weight: 700; width: 75%; transition: .2s; outline: none; border-bottom-color: #6A679E;', 'placeholder': "Имя"}))
    last_name = forms.CharField(label='Фамилия', required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3','style': 'border: none; border-bottom: 2px solid #D1D1D4; 	background: none; padding: 10px; padding-left: 24px; font-weight: 700; width: 75%; transition: .2s; outline: none; border-bottom-color: #6A679E;', 'placeholder': "Фамилия"}))
    position = forms.ModelChoiceField(label='Должность', queryset=Position.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control mb-3', 'style': 'display: block; width: 35%;  padding: 10px; background: rgba(224, 226, 225, 1); border-top: 1px solid rgba(0, 0, 0, .05); cursor: pointer; '}))
    phone = forms.CharField(label='Номер телефона', required=False, widget=forms.NumberInput(attrs={'class': 'form-control mb-3', 'style': 'border: none; border-bottom: 2px solid #D1D1D4; 	background: none; padding: 10px; padding-left: 24px; font-weight: 700; width: 75%; transition: .2s; outline: none; border-bottom-color: #6A679E;', 'placeholder': "Номер телефона"}))

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
                position=self.cleaned_data['position'],
                phone=self.cleaned_data['phone'],
            )
        return user
    


