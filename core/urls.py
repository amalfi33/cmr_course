from django.urls import path
from .import views
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

    path('course_create/', views.course_create, name='course_create'),
    path('course_list', views.course_list, name='course_list'),
    
    path('atendence/<str:code>/', views.attendance, name='atendence'),
]


