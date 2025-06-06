# Generated by Django 5.1.6 on 2025-02-16 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserRegistration_name', models.CharField(max_length=50)),
                ('UserRegistration_email', models.CharField(max_length=50)),
                ('UserRegistration_contact', models.CharField(max_length=50)),
                ('UserRegistration_address', models.CharField(max_length=50)),
                ('UserRegistration_gender', models.CharField(max_length=50)),
                ('UserRegistration_photo', models.FileField(upload_to='Assets/user/')),
                ('UserRegistration_password', models.CharField(max_length=50)),
            ],
        ),
    ]
