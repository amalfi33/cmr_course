from django.urls import path
from .import views
from .views import login_site


urlpatterns = [
    path('', views.home, name='home'),
    path('atendence/<str:code>/', views.attendance, name='atendence'),
    path('progress_crm/', views.index, name='index'),
    path('logout/', views.logout_site, name='logout'),
    path('', views.login_site, name='login'),
    path('', views.base, name='base'),
]


