from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/post/', views.createpost, name='createpost'),
    path('update/post/<str:pk>/', views.updatepost, name='updatepost'),
]