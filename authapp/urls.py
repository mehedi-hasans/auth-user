from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('loginPage', views.loginPage, name = 'loginPage'),
    path('dashboard', views.dashboard, name = 'dashboard')
]