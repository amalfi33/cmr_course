# Generated by Django 5.0.1 on 2024-02-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_teacher_name_teacher_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='employee',
        ),
        migrations.AddField(
            model_name='teacher',
            name='name',
            field=models.CharField(default=1, max_length=100, verbose_name='Ф.И.О'),
            preserve_default=False,
        ),
    ]
