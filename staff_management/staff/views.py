import pandas as pd

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

from .forms import EmployeeForm
from .models import Employee
from io import BytesIO

from urllib.parse import quote


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('employee_list')  # Перенаправить на страницу учета пользователей
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('employee_list')  # Перенаправить на страницу учета пользователей
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})


def employee_list(request):
    employees = Employee.objects.all().order_by('id')
    return render(request, 'employee_list.html', {'employees': employees})


def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})


def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
    return redirect('employee_list')


def export_to_excel(request):
    employees = Employee.objects.all().values()
    df = pd.DataFrame(employees)

    column_names_ru = {
        'id': 'ID',
        'last_name': 'Фамилия',
        'first_name': 'Имя',
        'middle_name': 'Отчество',
        'position': 'Должность',
        'department': 'Отдел',
        'hire_date': 'Дата приема',
        'birth_date': 'Дата рождения',
        'phone_number': 'Мобильный телефон',
        'email': 'Электронная почта',
        'address': 'Адрес проживания',
        'status': 'Статус',
        'projects': 'Комментарий',
    }
    df.rename(columns=column_names_ru, inplace=True)

    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Список сотрудников')
    output.seek(0)

    filename = "Список сотруднкиво.xlsx"
    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename*=UTF-8\'\'{quote(filename)}'

    return response
