from django.urls import path
from account import views
from django.contrib.auth import views as account_view

urlpatterns = [
    path('register/', views.registeruser, name='register'),
    path('profile/', views.profile, name='profile'),
    # path('update/profile/<str:pk>/', views.updateprofile, name='updateprofile'),

    path('login/', account_view.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', account_view.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
]