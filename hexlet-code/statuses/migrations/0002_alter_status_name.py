# Generated by Django 4.2.4 on 2023-09-26 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
