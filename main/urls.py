from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.index, name='index'),
    path('work/', views.work, name='work'),
    path('services/', views.services, name='services'),
    path('clients/', views.clients, name='clients'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/', views.profile_view, name='profile'),  
]