# Generated by Django 4.2.2 on 2023-07-20 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_rename_employee_emp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Emp',
            new_name='Employee',
        ),
    ]
