#from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.employee_create, name='employee_create'),
    path('list/', views.employee_list, name='employee_list'),
    path('export/', views.export_to_excel, name='export_to_excel'),
    path('edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('login/', views.login_view, name='login'),
    #path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
