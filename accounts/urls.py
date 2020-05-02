from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    path('register/', views.register_view, name="register_view"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('logout_view/', LogoutView.as_view(), name="logout_view"),
    path('reset_password/', auth_views.PasswordResetView.as_view()),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('edit_all/', views.edit_all, name='custmize'),

]
