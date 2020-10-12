from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path("", views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path("signin/", auth_views.LoginView.as_view(template_name='user/signin.html'), name='signin'),
    path("logout/", auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),

]
