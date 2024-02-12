from django.urls import path
from .import views
from .views import login_site


urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_site, name='logout'),
    path('login/', login_site, name='login_site'),
    path('accounts/login/', login_site, name='login_site'),
]


