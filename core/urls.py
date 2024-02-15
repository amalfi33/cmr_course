from django.urls import path
from .import views
from .views import login_site


urlpatterns = [
    path('atendence/<str:code>/', views.attendance, name='atendence'),
    path('', views.index, name='index'),
    path('logout/', views.logout_site, name='logout'),
    path('accounts/login/', views.login_site, name='login_site'),
]


