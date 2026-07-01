from django.urls import path
from .views import registration_view,signin_view,logout_view

urlpatterns = [
    path('login/',registration_view,name='registration_url'),
    path('signin/',signin_view,name='signin_url'),
    path('logout/',logout_view,name='logout_url'),
]