# Generated by Django 4.2 on 2024-03-11 07:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("studentmanagement", "0007_alter_studentattendance_leave_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentattendance",
            name="leave_type",
            field=models.CharField(
                choices=[
                    ("half_day", "Half day"),
                    ("full_day", "Full day"),
                    ("None", "None"),
                ],
                default="None",
                max_length=20,
                null=True,
            ),
        ),
    ]
