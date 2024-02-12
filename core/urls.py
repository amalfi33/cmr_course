from django.urls import path
from .import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('logout', views.logout_site, name='logout'),
    path('', views.login_site, name='login_site'),
]


