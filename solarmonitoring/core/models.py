from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_operator', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    is_operator = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']  # Обязательное поле при создании суперпользователя

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        permissions = [
            ("can_moderate", "Can moderate content"),
            ("can_view_analytics", "Can view analytics"),
        ]


class SolarStation(models.Model):
    objects = None
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stations')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.FloatField(help_text="Capacity in kW")
    installation_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.location})"


class SupportRequest(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


class EnergyData(models.Model):
    station = models.ForeignKey(SolarStation, on_delete=models.CASCADE, related_name='energy_data')
    timestamp = models.DateTimeField()
    generation = models.FloatField(default=0.0)
    temperature = models.FloatField(null=True, blank=True)
    efficiency = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = "Energy Data"


class SaleAdvertisement(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

from django.db import models

class Station(models.Model):
    # 1. Общие данные о системе
    name = models.CharField("Название системы", max_length=255)
    last_checked = models.DateTimeField("Время последней проверки", auto_now=True)
    location = models.TextField("Местоположение")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    system_type = models.CharField("Тип системы", max_length=50, choices=[
        ('Сетевая', 'Сетевая'),
        ('Гибридная', 'Гибридная'),
        ('Автономная', 'Автономная')
    ])
    installed_power = models.FloatField("Установленная мощность (кВт)")
    installation_date = models.DateField("Дата установки")

    # 2. Параметры солнечных панелей
    panel_count = models.PositiveIntegerField("Количество панелей")
    panel_type = models.CharField("Тип панелей", max_length=50, choices=[
        ('Монокристалл', 'Монокристалл'),
        ('Поликристалл', 'Поликристалл'),
        ('Тонкая плёнка', 'Тонкая плёнка')
    ])
    panel_power = models.FloatField("Мощность одной панели (Вт)")
    panel_manufacturer = models.CharField("Производитель панелей", max_length=255)
    tilt_angle = models.FloatField("Угол наклона")
    orientation = models.CharField("Ориентация", max_length=50)

    # 3. Инвертор
    inverter_type = models.CharField("Тип инвертора", max_length=50, choices=[
        ('Сетевой', 'Сетевой'),
        ('Гибридный', 'Гибридный'),
        ('Автономный', 'Автономный')
    ])
    inverter_power = models.FloatField("Мощность инвертора (кВт)")
    inverter_manufacturer = models.CharField("Производитель инвертора", max_length=255)
    controller_type = models.CharField("Тип контроллера", max_length=50, choices=[
        ('PWM', 'PWM'),
        ('MPPT', 'MPPT')
    ])

    # 4. Аккумуляторная система
    battery_type = models.CharField("Тип аккумуляторов", max_length=50, choices=[
        ('Свинцово-кислотные', 'Свинцово-кислотные'),
        ('AGM', 'AGM'),
        ('Гелевые', 'Гелевые'),
        ('Литиевые', 'Литиевые')
    ])
    battery_count = models.PositiveIntegerField("Количество аккумуляторов")
    battery_capacity_single = models.FloatField("Емкость одного аккумулятора (кВт·ч)")
    battery_voltage = models.CharField("Напряжение системы", max_length=10, choices=[
        ('12 В', '12 В'), ('24 В', '24 В'), ('48 В', '48 В')
    ])
    battery_manufacturer = models.CharField("Производитель", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Станция"
        verbose_name_plural = "Станции"