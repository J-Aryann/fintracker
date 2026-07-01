from django.urls import path
from .views import create_view,show_expence_view,update_expence,delete_view, dashboard

urlpatterns = [
    path('create/',create_view , name='create_expence_view_url'),
    path('show/',show_expence_view,name='show_expence_view_url'),
    path('update/<int:pk>',update_expence,name='update_expence_url'),
    path('delete/<int:pk>/',delete_view,name='delete_url'),


    path('d/',dashboard,name='d_url'),

]