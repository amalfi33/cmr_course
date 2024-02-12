from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', views.base, name='base'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    path('login',views.login_site, name = 'login '),
]


