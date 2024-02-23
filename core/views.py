from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm
from .models import Course, Teacher, Student , Employee , Position , Group
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import TeacherForm , CourseForm, StudentForm , EmployeeCreationForm
from django.http import HttpResponse
from django.contrib import messages
import qrcode
from .models import  Course
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
        position = Position.objects.all()
        courses = Course.objects.all()
        context = {'courses': courses ,'employees': employees ,'position': position}
        return render(request, 'index.html', context)
    return redirect('login')

# --------КУРСЫ---------

# ----------------------------------
@staff_member_required
def create_course(request):
    if request.method == 'POST':
        course = Course()
        course.title = request.POST.get('title')
        new_slug = slugify(request.POST.get('title'))
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            course.image = filename
        course.description = request.POST.get('description')
        course.save()
        return redirect('index')  # Предполагается, что у вас есть URL с именем 'index'
    return render(request, 'create_course.html')
# ----------------------------------



# ----------------------------------
@staff_member_required
def delete_course(request, course_id, slug):
    course = get_object_or_404(Course, id=course_id)

    course = Course.objects.get(slug__exact=slug)
    course.delete()
    return redirect('index')
# ----------------------------------



# ----------------------------------
@staff_member_required
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeCreationForm()
    return render(request, 'register.html', {'form': form})
# ----------------------------------


def position(request):
    positions = Position.objects.all()
    return render(request, 'index.html', {'positions': positions})

def employee(request):
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees})

def teacher(request):
    teachers = Teacher.objects.all()
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


    
    



# Ученик
@staff_member_required 
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
           
            student.save()
            return redirect('index.html')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})
# ----------------------------------


# ----------------------------------
@staff_member_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        student.delete()
        return redirect('index.html')
    
    return render(request, 'delete_student.html', {'student': student})
# ----------------------------------


@staff_member_required
def employee_create(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()
            
            # Создаем объект Employee
            employee = Employee.objects.create(user=user, phone=form.cleaned_data['phone'])
            
            # Назначаем должность (position) для сотрудника
            positions = form.cleaned_data['position']  # Получаем выбранные должности из формы
            employee.position.set(positions)  # Назначаем выбранные должности сотруднику
            
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})






# ----------------------------------
@staff_member_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'edit_student.html', {'form': form})


def attendance(request):
    return redirect(request,)
# ----------------------------------


# Учитель


# ----------------------------------
@staff_member_required
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = TeacherForm()
    
    return render(request, 'create_teacher.html', {'form': form})
# ----------------------------------


# ----------------------------------
@staff_member_required
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    if request.method == 'POST':
        teacher.delete()
        return redirect('index.html')
    
    return render(request, 'delete_teacher.html', {'teacher': teacher})
# ----------------------------------


# ----------------------------------
@staff_member_required
def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = TeacherForm(instance=teacher)
    
    return render(request, 'edit_teacher.html', {'form': form})
# ----------------------------------





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

    return render(request, 'home.html')

# @login_required  требует чтобы пользователь был аутентифицирован, чтобы использовать функцию logout_site.


