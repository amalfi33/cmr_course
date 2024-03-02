from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm
from .models import Course, Specialty, Student , Employee , Position , Group
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CourseForm,  EmployeeCreationForm , GroupCreateForm, EmployeeEditForm
import qrcode
from .models import  Course
from django.utils import timezone
from django.utils.text import slugify
from django.core.files.storage import FileSystemStorage
from random import randint
from django.contrib.auth.decorators import user_passes_test
from .models import Profile

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




# Сотрудник
@staff_member_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
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
        return redirect('index')

@staff_member_required
def employee_edit(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':

        form = EmployeeEditForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeEditForm(instance=employee)
    return render(request, 'employee_edit.html', {'form': form})

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


# ----------------------------------
    


# Группы
@staff_member_required
def group_list(request):
    groups = Group.objects.all()
    return render( request, 'group_list.html', {'groups': groups})


@staff_member_required
def group_create(request):
    if request.method =='POST':
        form = GroupCreateForm()
        if form.is_valid():
            form.save()
        return redirect('group_list')
    else:
        form = GroupCreateForm()
        return render(request, 'group_create.html', {'form': form })
    
def group_delete(request , group_id ):
    group = get_object_or_404(Group , id=group_id)
    if request.method == 'POST':
        group.delete()
        return redirect('group_list')


    
    


def position(request):
    positions = Position.objects.all()
    return render(request, 'index.html', {'positions': positions})

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
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})

# @login_required  требует чтобы пользователь был аутентифицирован, чтобы использовать функцию logout_site.


# Профиль 


def profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profile.html', {'profile': profile})


