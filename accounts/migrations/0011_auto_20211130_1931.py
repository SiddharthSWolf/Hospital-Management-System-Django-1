# Generated by Django 3.1.7 on 2021-11-30 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20211130_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorprofile',
            name='password',
        ),
        migrations.RemoveField(
            model_name='patientprofile',
            name='password',
        ),
        migrations.RemoveField(
            model_name='staffprofile',
            name='password',
        ),
    ]
