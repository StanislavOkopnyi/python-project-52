# Generated by Django 4.2.4 on 2023-11-16 14:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("labels", "0002_label_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="label",
            name="task",
        ),
    ]
