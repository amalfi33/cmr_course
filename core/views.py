from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm
from .models import Course, Teacher, Student
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import TeacherForm
from django.http import HttpResponse
import qrcode


# @staff_member_required Нужен для того чтобы добавлять ученика или курс мог только администратор !!!!


def index(request):
    return render(request, 'index.html')

# --------КУРСЫ---------

# ----------------------------------
@staff_member_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})
# ----------------------------------



# ----------------------------------
@staff_member_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        course.delete()
        return redirect('index.html')
    
    return render(request, 'delete_course.html', {'course': course})
# ----------------------------------



# ----------------------------------
# @staff_member_required
# def edit_course(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
    
#     if request.method == 'POST':
#         form = CourseForm(request.POST, instance=course)
#         if form.is_valid():
#             form.save()
#             return redirect('index.html')
#     else:
#         form = CourseForm(instance=course)
    
#     return render(request, 'edit_course.html', {'form': form})
# ----------------------------------


# Ученик

# ----------------------------------
# @staff_member_required 
# def create_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             student = form.save(commit=False)
           
#             student.save()
#             return redirect('index.html')
#     else:
#         form = StudentForm()
#     return render(request, 'create_student.html', {'form': form})
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
# @staff_member_required
# def edit_student(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
    
#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('index.html')
#     else:
#         form = StudentForm(instance=student)
    
#     return render(request, 'edit_student.html', {'form': form})
# def attendance(request):
#     return render(request)
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
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            message = 'Имя пользоватаеля или пароль не верный!!!!!!!!!!!'
            return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')

def logout_site(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')




