from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('task/add/', views.add_task, name='add_task'),
    path('task/<int:pk>/edit/', views.edit_task, name='edit_task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
]
