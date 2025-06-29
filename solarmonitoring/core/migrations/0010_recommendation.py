# Generated by Django 5.2.1 on 2025-06-18 00:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_station_force_attention_until_station_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('text', models.TextField(verbose_name='Рекомендация')),
                ('recommendation_type', models.CharField(choices=[('maintenance', 'Техническое обслуживание'), ('upgrade', 'Обновление оборудования'), ('inspection', 'Плановый осмотр'), ('cleaning', 'Очистка панелей')], max_length=20, verbose_name='Тип')),
                ('status', models.CharField(choices=[('pending', 'Ожидает'), ('in_progress', 'В процессе'), ('completed', 'Выполнено')], default='pending', max_length=20, verbose_name='Статус')),
            ],
        ),
    ]
