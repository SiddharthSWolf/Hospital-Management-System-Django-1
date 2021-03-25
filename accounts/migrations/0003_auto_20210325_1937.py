# Generated by Django 3.1.7 on 2021-03-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210325_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprofile',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='doctor_full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='profile_picture',
            field=models.ImageField(upload_to='profile_pictures/doctor_profile_picture/'),
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='speciality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='diagnosis',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='profile_picture',
            field=models.ImageField(upload_to='profile_pictures/patient_profile_picture/'),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='date_joined',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='profile_picture',
            field=models.ImageField(upload_to='profile_pictures/staff_profile_picture/'),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='qualification',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='staff_full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]