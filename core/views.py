from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm
from .models import Course, Specialty, Student , Employee , Group
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CourseForm,  EmployeeCreationForm , StudentForm
import qrcode
from .models import  Course
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.core.files.storage import FileSystemStorage
from random import randint
from django.contrib.auth.decorators import user_passes_test

# @staff_member_required Нужен для того чтобы добавлять ученика или курс мог только администратор !!!!

@login_required
def index(request):
    if request.user.is_authenticated:
        employees = Employee.objects.all()
        employeechoices = Employee.EmployeeStatus.choices
        courses = Course.objects.all()
        specialties = Specialty.objects.all()
        context = {'courses': courses ,'employees': employees ,'employeechoices': employeechoices, 'specialties': specialties}
        return render(request, 'index.html', context)
    return redirect('index')

# Сотрудник
@staff_member_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeCreationForm()
    return render(request, 'employee_create.html', {'form': form})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


@staff_member_required
def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')

@staff_member_required
def employee_edit(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        specialty_id = request.POST['specialty']
        position = request.POST['position']
        user = employee.user
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        employee.phone = phone
        employee.specialty = Specialty.objects.get(pk=specialty_id)
        employee.position = position
        employee.save()
        return redirect('employee_list')
    else:
        specialties = Specialty.objects.all()
        context = {
            'employee': employee,
            'specialties': specialties,
        }
        return render(request, 'employee_edit.html', context)



# ----------------------------------

# Курсы
@staff_member_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course_create.html', {'form': form})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

@staff_member_required
def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')

@staff_member_required
def course_edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        course.name = name
        course.price = price
        course.description = description
        course.save()
        return redirect('course_list')
    return render(request, 'course_edit.html', {'course': course})




# ----------------------------------
    


# Группы
@staff_member_required
def group_list(request):
    groups = Group.objects.all()
    return render( request, 'group_list.html', {'groups': groups})


@staff_member_required
def group_create(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        employee = request.POST.get('employee')
        course = request.POST.get('course')
        students = request.POST.getlist('students')
        
        group = Group.objects.create(
            name=name,
            employee=Employee.objects.get(pk=employee),
            course=Course.objects.get(pk=course)
        )
        group.students.add(*students)
        return redirect('group_list')
    else:
        employees = Employee.objects.all()
        students = Student.objects.all()
        courses = Course.objects.all()
        context = {
            'employees': employees,
            'students': students,
            'courses': courses
        }
        return render(request, 'group_create.html', context)

    
def group_delete(request , group_id ):
    group = get_object_or_404(Group , id=group_id)
    if request.method == 'POST':
        group.delete()
        return redirect('group_list')
    



# Студенты
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})




def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():

            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password']
            )

            student = form.save(commit=False)
            student.user = user
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_create.html', {'form': form})


    
    




def employee(request):
    employees = Employee.objects.all()
    return redirect(request, 'employee_delete', {'employees': employees})

def teacher(request):
    teachers = Specialty.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def course(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def student(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def group(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})

@staff_member_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        student.delete()
        return redirect('index.html')
    
    return render(request, 'delete_student.html', {'student': student})


def attendance(request):
    return redirect(request,)






# Авторизация
def login_site(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'base.html', {'error_message': 'Неверное имя пользователя или пароль.'})
    return render(request, 'base.html')



# @login_required  требует чтобы пользователь был аутентифицирован, чтобы использовать функцию logout_site.
@login_required
def logout_site(request):
    logout(request)
    return redirect('login')

    

def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})

# @login_required  требует чтобы пользователь был аутентифицирован, чтобы использовать функцию logout_site.


# Профиль 


def profile(request, id)    :
    profile = Employee.objects.get(user_id__exact = id)
    return render(request, 'profile.html', {'profile': profile})


