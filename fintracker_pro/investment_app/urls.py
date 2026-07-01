from django.urls import path
from .views import create_investment , show_investment,update_view,delete_view,dashboard_investment

urlpatterns =[
    path('create/',create_investment,name='create_investment_url'),
    path('show/',show_investment,name='show_investment_url'),
    path('update_invest/<int:pk>/',update_view,name='update_view_url'),
    path('delete_invest/<int:pk>/',delete_view,name='investment_delete_view_url'),
    path('dash/',dashboard_investment,name='dashboard_url')
]