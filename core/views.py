from django.shortcuts import render ,  redirect
from django.contrib.auth import authenticate , login , logout


def index(request):
    return render(request, 'index.html')

# Курсы
def create_course(request):
    return render(request)

def delete_course(request):
    return render(request)

def edit_course(request):
    return render(request)   

# Ученик
def create_student(request):
    return render(request)

def delete_student(request):
    return render(request)

def edit_student(request):
    return render(request)

def attendance(request):
    return render(request)

# Учитель
def create_teacher(request):
    return render(request)

def delete_teacher(request):
    return render(request)

def edit_teacher(request):
    return render(request)

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

