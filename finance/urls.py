from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/add/', views.transaction_create, name='transaction_create'),
    path('transactions/<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),
    path('goals/', views.goal_list, name='goal_list'),
    path('goals/add/', views.goal_create, name='goal_create'),
]
