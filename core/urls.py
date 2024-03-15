from django.urls import path
from . import views
from .views import login_site


urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    
    path('logout/', views.logout_site, name='logout'),
    path('login/', views.login_site, name='login'),

    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee_create/', views.employee_create, name='employee_create'),
    path('employee_edit/<int:employee_id>/', views.employee_edit, name='employee_edit'),
    path('employee_delete/<int:employee_id>/', views.employee_delete, name='employee_delete'),

    path('profile/<int:id>/', views.profile, name='profile'),

    path('course_create/', views.course_create, name='course_create'),
    path('course_list', views.course_list, name='course_list'),
    path('course_delete/<int:course_id>/delete', views.course_delete, name='course_delete'),
    path('course_edit/<int:course_id>/edit', views.course_edit, name = 'course_edit'),

    path('group_create/', views.group_create, name='group_create'),
    path('group_list/', views.group_list, name='group_list'),
    path('group_delete/<int:group_id>', views.group_delete, name='group_delete'),

    path('student_create/', views.student_create, name='student_create'),
    path('student_list/', views.student_list, name='student_list'),

    path('atendence/<str:code>/', views.attendance, name='atendence'),
]


