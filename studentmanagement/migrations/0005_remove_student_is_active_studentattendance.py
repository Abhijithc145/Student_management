# Generated by Django 4.2 on 2024-03-11 07:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("studentmanagement", "0004_alter_student_mark"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="is_active",
        ),
        migrations.CreateModel(
            name="StudentAttendance",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("date", models.DateField()),
                ("is_present", models.BooleanField(default=True)),
                (
                    "leave_type",
                    models.CharField(
                        choices=[("half_day", "Half day"), ("full_day", "Full day")],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="studentmanagement.student",
                    ),
                ),
            ],
        ),
    ]
