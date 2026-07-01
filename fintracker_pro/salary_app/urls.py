from django.urls import path
from .views import create_salary,show_salary,update_view,delete_view,salary_dashboard

urlpatterns = [
    path('create/',create_salary,name='cerate_salary_url'),
    path('show/',show_salary,name='show_salary_url'),
    path('update/<int:pk>/',update_view,name='update_url'),
    path('delete/<int:pk>/',delete_view,name='salary_delte_view_url'),
    path('dashboard/',salary_dashboard,name='salary_dashboard_url'),
]