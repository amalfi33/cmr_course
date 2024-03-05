# Generated by Django 4.2.7 on 2024-03-05 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_employee_position_alter_employee_specialty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('admin', 'Администратор'), ('teacher', 'Учитель')], max_length=20, verbose_name='Должность'),
        ),
    ]