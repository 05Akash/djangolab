# Generated by Django 5.0.6 on 2024-07-10 06:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("part3", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="student",
        ),
        migrations.RemoveField(
            model_name="student",
            name="email",
        ),
        migrations.DeleteModel(
            name="Course",
        ),
        migrations.DeleteModel(
            name="Project",
        ),
    ]
