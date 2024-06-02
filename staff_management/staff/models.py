from django.db import models


class Employee(models.Model):
    POSITION_CHOICES = [
        ('Продавец-кассир', 'Продавец-кассир'),
        ('Приёмщик товара', 'Приёмщик товара'),
        ('Комплектовщик', 'Комплектовщик'),
        ('Сборщик', 'Сборщик заказов'),
        ('Дир. магазина', 'Директор магазина'),
        ('Зам. директора', 'Заместитель директора'),
        ('Кладовщик', 'Кладовщик'),
        ('Охранник', 'Сотрудники службы безопасности'),
        ('Уборщик', 'Уборщик '),
        ('Сис. админ', 'Системный администратор'),
        ('Менеджер', 'Менеджер по персоналу '),
        ('Бухгалтер', 'Бухгалтер'),
    ]

    DEPARTMENT_CHOICES = [
        ('Отдел продаж', 'Отдел продаж'),
        ('Тех. отдел', 'Технический отдел'),
        ('Отдел кадров', 'Отдел кадров'),
        ('Экн. отдел', 'Финансово-экономический отдел'),
        ('Отдел безопасности', 'Отдел безопасности'),
        ('Складской отдел', 'Складской отдел'),
        ('Отдел приёма товара', 'Отдел приёма товара'),
    ]

    STATUS_CHOICES = [
        ('Работает', 'Работает'),
        ('Уволен', 'Уволен'),
    ]

    id = models.AutoField(primary_key=True, verbose_name='ID')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    middle_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество')
    position = models.CharField(max_length=100, choices=POSITION_CHOICES, verbose_name='Должность')
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES, verbose_name='Отдел')
    hire_date = models.DateField(verbose_name='Дата приема на работу')
    birth_date = models.DateField(verbose_name='Дата рождения')
    phone_number = models.CharField(max_length=15, verbose_name='Мобильный телефон')
    email = models.EmailField(verbose_name='Электронная почта')
    address = models.CharField(max_length=255, verbose_name='Адрес проживания')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Статус')
    projects = models.TextField(blank=True, null=True, verbose_name='Комментарий')

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
