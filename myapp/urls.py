from django.urls import path
from . import views
from .views import signup, home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.index, name="myapp_main_view"),
    path('signup/', signup, name='signup'),
    path('',    home,   name='home'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='myapp/login.html'),
        name='login'
    ),
    path('add/', views.create_user, name='create_user_api'),
    ]