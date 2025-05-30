# Generated by Django 5.1.6 on 2025-03-15 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0006_tbl_course_tbl_educationtype_delete_tbl_language_and_more'),
        ('Guest', '0011_initial'),
        ('User', '0023_delete_tbl_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Education_Institution', models.CharField(max_length=50)),
                ('Education_StartDate', models.CharField(max_length=50)),
                ('Education_EndDate', models.CharField(max_length=50)),
                ('Education_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_userregistration')),
            ],
        ),
    ]
